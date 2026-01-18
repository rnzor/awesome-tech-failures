#!/usr/bin/env python3
"""
Sync markdown entries to agent/entries.ndjson.
Parses YAML frontmatter and markdown body sections to generate structured data.
Warning: Overwrites agent/entries.ndjson
"""

import json
import re
import sys
import yaml
from pathlib import Path

def parse_markdown_entry(header_text, text_block, category_default):
    """Parse a single entry's frontmatter and body."""
    # Split YAML and Body
    yaml_match = re.search(r'```yaml\s*\n---\s*\n(.*?)\n---\s*\n', text_block, re.DOTALL)
    if not yaml_match:
        return None
        
    frontmatter_raw = yaml_match.group(1)
    body_raw = text_block[yaml_match.end():]
    
    try:
        data = yaml.safe_load(frontmatter_raw)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None

    if not data:
        data = {}

    # 1. Basic Metadata from Header
    header_text = header_text[4:].strip() if header_text.startswith('### ') else header_text.strip()
    year_match = re.search(r'^\((\d{4})\)', header_text)
    if year_match:
        data['year'] = int(year_match.group(1))
        title = header_text[year_match.end():].strip().lstrip('—-').strip()
        data['title'] = title
    else:
        if 'year' not in data:
            data['year'] = 2026
        data['title'] = header_text

    # 2. Extract Body Sections
    # Summary
    if 'summary' not in data:
        summary_match = re.search(r'\*\*What happened:\*\*\s*(.*?)(?:\s*\n\s*\*\*|$)', body_raw, re.DOTALL)
        if summary_match:
            data['summary'] = summary_match.group(1).strip().replace('\n', ' ')
    
    # Root Cause
    if 'root_cause' not in data and 'root-cause' not in data:
        rc_match = re.search(r'\*\*Root cause:\*\*\s*(.*?)(?:\s*\n\s*\*\*|$)', body_raw, re.DOTALL)
        if rc_match:
            data['root_cause'] = rc_match.group(1).strip().replace('\n', ' ')
    
    # Lessons
    if 'lessons' not in data or not data['lessons']:
        lessons_section = re.search(r'\*\*Lessons:\*\*\s*\n((?:(?!\n\n).)*)', body_raw, re.DOTALL)
        if lessons_section:
            data['lessons'] = [line.strip()[2:].strip() for line in lessons_section.group(1).split('\n') if line.strip().startswith('- ')]
            
    # Patterns
    if 'patterns' not in data or not data['patterns']:
        patterns_section = re.search(r'\*\*Related failure patterns:\*\*\s*\n((?:(?!\n\n).)*)', body_raw, re.DOTALL)
        if patterns_section:
            data['patterns'] = [line.strip()[2:].strip() for line in patterns_section.group(1).split('\n') if line.strip().startswith('- ')]

    # 3. Schema Alignment & Normalization
    
    # Category (from type in frontmatter)
    if 'type' in data:
        data['category'] = data.pop('type')
    if 'category' not in data:
        data['category'] = category_default

    # Root Cause key
    if 'root-cause' in data:
        data['root_cause'] = data.pop('root-cause')
    if 'root_cause' not in data:
        data['root_cause'] = "Not specified."

    # Evidence Type mapping (hyphen to underscore)
    ev_type = data.pop('evidence-type', data.get('evidence_type', 'direct_incident'))
    data['evidence_type'] = str(ev_type).replace('-', '_')

    # Impact (ensure list)
    impact = data.get('impact', [])
    if isinstance(impact, str):
        data['impact'] = [impact]
    elif not isinstance(impact, list):
        data['impact'] = []

    # Severity normalization
    severity = data.get('severity', {})
    if isinstance(severity, str):
        severity = {"level": severity}
    elif not severity:
        severity = {"level": "medium"}
    if 'score' in severity and severity['score'] is not None:
        try: severity['score'] = int(severity['score'])
        except: del severity['score']
    data['severity'] = severity

    # Sources (Array of Objects)
    sources = data.get('sources', [])
    new_sources = []
    if isinstance(sources, list):
        for src in sources:
            if isinstance(src, str):
                new_sources.append({"title": "Source", "url": src, "kind": "primary"})
            elif isinstance(src, dict) and 'url' in src:
                src.setdefault('title', "Source")
                src.setdefault('kind', "primary")
                new_sources.append(src)
    data['sources'] = new_sources

    # Required lists initialization
    for field in ['lessons', 'patterns', 'tags']:
        if field not in data or not isinstance(data[field], list):
            data[field] = []

    # Summary length check (schema maxLength: 200)
    if 'summary' not in data:
        data['summary'] = "Summary not provided."
    if len(data['summary']) > 200:
        data['summary'] = data['summary'][:197] + "..."

    # ID Generation
    if 'id' not in data:
        slug = re.sub(r'[^a-z0-9]+', '-', data['title'].lower()).strip('-')
        data['id'] = f"{slug}-{data.get('year', 'xxxx')}"

    # Clean non-schema fields
    data.pop('source_ids', None)
    data.pop('supporting-entities', None)
    data.pop('supporting_entities', None)
    
    return data

def main():
    repo_root = Path(__file__).parent.parent
    mapping = {
        'ai-slop-and-automation.md': 'ai-slop',
        'production-outages.md': 'outage',
        'security-incidents.md': 'security',
        'startup-failures.md': 'startup',
        'product-failures.md': 'product',
        'decision-failures.md': 'decision',
    }
    
    output_entries = []
    
    for filename, category_default in mapping.items():
        file_path = repo_root / filename
        if not file_path.exists():
            continue
            
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        current_entry_lines = []
        current_header = None
        
        for line in lines:
            if line.startswith('### '):
                if current_entry_lines and current_header:
                    text_block = '\n'.join(current_entry_lines)
                    entry = parse_markdown_entry(current_header, text_block, category_default)
                    if entry: output_entries.append(entry)
                current_header = line
                current_entry_lines = []
            elif current_header:
                current_entry_lines.append(line)
        
        if current_entry_lines and current_header:
            text_block = '\n'.join(current_entry_lines)
            entry = parse_markdown_entry(current_header, text_block, category_default)
            if entry: output_entries.append(entry)

    outfile = repo_root / 'agent' / 'entries.ndjson'
    with open(outfile, 'w', encoding='utf-8') as f:
        for entry in output_entries:
            f.write(json.dumps(entry) + '\n')
            
    print(f"Successfully wrote {len(output_entries)} entries to {outfile}")

if __name__ == '__main__':
    main()
