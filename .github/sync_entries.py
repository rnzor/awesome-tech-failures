#!/usr/bin/env python3
"""
Sync markdown entries to agent/entries.ndjson.

This script parses the YAML frontmatter from markdown entry files and
outputs a synchronized NDJSON file for the agent layer.

Note: This is a partial sync that logs entries found. Full implementation
would parse complete entry structure including lessons and sources.
"""

import json
import re
import sys
from pathlib import Path


def extract_yaml_blocks(content: str) -> list[dict]:
    """Extract YAML blocks from markdown content."""
    # Pattern to match ```yaml ... ``` blocks
    pattern = r'```yaml\s*\n---\s*\n(.*?)\n---\s*\n(.*?)```'
    matches = re.findall(pattern, content, re.DOTALL)
    
    entries = []
    for frontmatter, body in matches:
        entry = {}
        
        # Parse frontmatter (simple key: value parsing)
        for line in frontmatter.strip().split('\n'):
            if ':' in line:
                key, _, value = line.partition(':')
                key = key.strip()
                value = value.strip()
                
                # Handle arrays
                if value.startswith('[') and value.endswith(']'):
                    value = [v.strip() for v in value[1:-1].split(',')]
                
                entry[key] = value
        
        # Extract lessons from body
        lessons = []
        in_lessons = False
        for line in body.split('\n'):
            if '**Lessons:**' in line:
                in_lessons = True
                continue
            if in_lessons and line.strip().startswith('-'):
                lessons.append(line.strip()[1:].strip())
            elif in_lessons and line.strip().startswith('**'):
                in_lessons = False
        
        if lessons:
            entry['lessons'] = lessons
        
        # Extract source URL
        source_match = re.search(r'\*\*Source:\*\*\s*(https?://[^\s]+)', body)
        if source_match:
            entry['primary_source'] = source_match.group(1)
        
        entries.append(entry)
    
    return entries


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
    
    all_entries = []
    
    for filename in category_files:
        file_path = repo_root / filename
        if not file_path.exists():
            continue
        
        content = file_path.read_text(encoding='utf-8')
        entries = extract_yaml_blocks(content)
        
        print(f"Found {len(entries)} entries in {filename}")
        all_entries.extend(entries)
    
    print(f"\nTotal entries found: {len(all_entries)}")
    print("Note: Full sync would write to agent/entries.ndjson")
    print("Currently, entries.ndjson is maintained manually for quality control.")
    
    # For now, just validate that we can parse entries
    # Full implementation would write to entries.ndjson
    return 0


if __name__ == '__main__':
    sys.exit(main())
