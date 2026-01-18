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


def parse_markdown_entry(frontmatter_raw, body_raw):
    """Parse a single entry's frontmatter and body."""
    try:
        data = yaml.safe_load(frontmatter_raw)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None

    # Normalization
    if not data:
        return None

    # Extract Summary (What happened)
    # Matches text between **What happened:** and next section (**Impact:** or **Root cause:**)
    summary_match = re.search(r'\*\*What happened:\*\*\s*(.*?)\s*\n\s*\*\*', body_raw, re.DOTALL)
    if summary_match:
        data['summary'] = summary_match.group(1).strip().replace('\n', ' ')

    # Extract Root Cause
    root_cause_match = re.search(r'\*\*Root cause:\*\*\s*(.*?)\s*\n\s*\*\*', body_raw, re.DOTALL)
    if root_cause_match:
        data['root-cause'] = root_cause_match.group(1).strip().replace('\n', ' ')

    # Extract Lessons
    lessons_section = re.search(r'\*\*Lessons:\*\*\s*\n((?:(?!\n\n).)*)', body_raw, re.DOTALL)
    if lessons_section:
        raw_lessons = lessons_section.group(1)
        lessons = []
        for line in raw_lessons.split('\n'):
            line = line.strip()
            if line.startswith('- '):
                 lessons.append(line[2:].strip())
        if lessons:
            data['lessons'] = lessons

    # Ensure required array fields exist
    if 'lessons' not in data:
        data['lessons'] = []
    
    # Generate ID if missing (from title)
    # Most entries seem to lack 'id' in frontmatter in the new ones?
    # Actually, existing schema requires ID. My new entries didn't specify 'id' in yaml!
    # I need to generate it or extract it.
    # The entries usually don't have ID in YAML? Let's check existing files.
    
    # Wait, looking at `entries.ndjson`, they have "id".
    # Looking at `ai-slop-and-automation.md`:
    # 
    # ### (2016) Microsoft Tay ...
    # ```yaml
    # ---
    # type: ...
    # ---
    #
    # It seems ID is NOT in the frontmatter. I must generate it.
    
    # Heuristic for ID: lowercase-kebab-title-year
    # But wait, looking at my edit to decision-failures.md:
    # ### (2019) Boeing 737 MAX MCAS — ...
    # Title is complex.
    
    # Let's try to infer ID from the markdown header if available?
    # My script splits by `### `. I will pass the header line to this function.
    
    return data

def main():
    repo_root = Path(__file__).parent.parent
    category_files = [
        'ai-slop-and-automation.md',
        'production-outages.md',
        'security-incidents.md',
        'startup-failures.md',
        'product-failures.md',
        'decision-failures.md',
    ]
    
    output_entries = []
    
    for filename in category_files:
        file_path = repo_root / filename
        if not file_path.exists():
            continue
            
        content = file_path.read_text(encoding='utf-8')
        
        # Split by ### headers
        # We need the header line to extract Year and Title
        
        # Regex to find entries:
        # ### (Year) Title
        # ... content ...
        
        # We'll stick to splitting by line for simplicity but capture the header
        lines = content.split('\n')
        current_entry_lines = []
        current_header = None
        
        for line in lines:
            if line.startswith('### '):
                # Process previous
                if current_entry_lines and current_header:
                    text_block = '\n'.join(current_entry_lines)
                    # Extract YAML
                    yaml_match = re.search(r'```yaml\s*\n---\s*\n(.*?)\n---\s*\n', text_block, re.DOTALL)
                    if yaml_match:
                        frontmatter = yaml_match.group(1)
                        # Body is everything after YAML end
                        body = text_block[yaml_match.end():]
                        
                        entry_data = parse_markdown_entry(frontmatter, body)
                        if entry_data:
                            # Parse header for metadata
                            # Header format: ### (YYYY) Title...
                            # or ### Title...
                            header_text = current_header[4:].strip()
                            
                            # Try to extract year: (YYYY)
                            year_match = re.search(r'^\((\d{4})\)', header_text)
                            if year_match:
                                entry_data['year'] = int(year_match.group(1))
                                # Title is the rest
                                title_part = header_text[year_match.end():].strip()
                                # Remove starting dash if present (e.g. ") - Title")
                                if title_part.startswith('—') or title_part.startswith('-'):
                                    title_part = title_part[1:].strip()
                                entry_data['title'] = title_part
                            else:
                                if 'year' not in entry_data:
                                    entry_data['year'] = 2026 # Default? Or leave out? Schema requires year.
                                entry_data['title'] = header_text

                            # Generate ID if missing
                            if 'id' not in entry_data:
                                # Create slug from title
                                slug = re.sub(r'[^a-z0-9]+', '-', entry_data['title'].lower()).strip('-')
                                entry_data['id'] = f"{slug}-{entry_data.get('year', 'xxxx')}"

                            output_entries.append(entry_data)

                current_header = line
                current_entry_lines = []
            elif current_header:
                current_entry_lines.append(line)
        
        # Process last entry
        if current_entry_lines and current_header:
            text_block = '\n'.join(current_entry_lines)
            yaml_match = re.search(r'```yaml\s*\n---\s*\n(.*?)\n---\s*\n', text_block, re.DOTALL)
            if yaml_match:
                frontmatter = yaml_match.group(1)
                body = text_block[yaml_match.end():]
                entry_data = parse_markdown_entry(frontmatter, body)
                if entry_data:
                    header_text = current_header[4:].strip()
                    year_match = re.search(r'^\((\d{4})\)', header_text)
                    if year_match:
                        entry_data['year'] = int(year_match.group(1))
                        title_part = header_text[year_match.end():].strip()
                        if title_part.startswith('—') or title_part.startswith('-'):
                             title_part = title_part[1:].strip()
                        entry_data['title'] = title_part
                    else:
                        if 'year' not in entry_data:
                            entry_data['year'] = 2026 
                        entry_data['title'] = header_text

                    if 'id' not in entry_data:
                        slug = re.sub(r'[^a-z0-9]+', '-', entry_data['title'].lower()).strip('-')
                        entry_data['id'] = f"{slug}-{entry_data.get('year', 'xxxx')}"
                    
                    output_entries.append(entry_data)

    # Write to ndjson
    outfile = repo_root / 'agent' / 'entries.ndjson'
    with open(outfile, 'w', encoding='utf-8') as f:
        for entry in output_entries:
            f.write(json.dumps(entry) + '\n')
            
    print(f"Successfully wrote {len(output_entries)} entries to {outfile}")

if __name__ == '__main__':
    main()
