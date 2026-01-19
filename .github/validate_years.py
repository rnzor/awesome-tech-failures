#!/usr/bin/env python3
"""Validate year consistency between headers and NDJSON."""

import json
import re
import sys
from pathlib import Path

def extract_header_year(header):
    """Extract expected year from header."""
    # Pattern 1: Date range (2023-2024) - use END year
    range_match = re.search(r'\((\d{4})[-–u2013](\d{4})\)', header)
    if range_match:
        return int(range_match.group(2))
    
    # Pattern 2: Single year (2024)
    single_match = re.search(r'\((\d{4})\)', header)
    if single_match:
        return int(single_match.group(1))
        
    return None

def main():
    repo_root = Path(__file__).parent.parent
    entries_file = repo_root / 'agent' / 'entries.ndjson'
    
    if not entries_file.exists():
        print(f"Error: {entries_file} not found")
        return 1

    errors = []
    warnings = []
    
    print(f"Validating years in {entries_file}...", file=sys.stderr)
    
    with open(entries_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            if not line.strip(): continue
            
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                errors.append(f"Line {line_num}: Invalid JSON")
                continue

            title = entry.get('title', '')
            stored_year = entry.get('year')
            entry_id = entry.get('id', 'unknown')
            
            # Check for null year
            if stored_year is None:
                errors.append(f"Line {line_num} [{entry_id}]: NULL year. Header: '{title}'")
                continue
            
            # Check consistency with header if header contains a year
            header_year = extract_header_year(title)
            if header_year and header_year != stored_year:
                 # Allow start year from range if it makes sense, but strictly we want END year
                 errors.append(f"Line {line_num} [{entry_id}]: Year mismatch. Stored: {stored_year}, Expected from header: {header_year}")

            # Check for suspicious 2026 (old fallback)
            if stored_year == 2026 and '2026' not in title and 'Ongoing' not in title:
                warnings.append(f"Line {line_num} [{entry_id}]: Suspicious 2026 year. Header: '{title}'")

    if warnings:
        print("\nWarnings (Suspicious Years):")
        for w in warnings:
            print(f"  - {w}")

    if errors:
        print("\nErrors (Invalid/Missing Years):")
        for e in errors:
            print(f"  - {e}")
        return 1
        
    print("\nYear validation passed!")
    return 0

if __name__ == '__main__':
    sys.exit(main())
