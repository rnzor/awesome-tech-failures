#!/usr/bin/env python3
"""
Validate pattern references in markdown entries.
Ensures all pattern IDs referenced in entries exist in patterns.ndjson.
"""

import json
import re
import sys
from pathlib import Path


def load_valid_pattern_ids(repo_root: Path) -> set:
    """Load all valid pattern IDs from patterns.ndjson."""
    patterns_file = repo_root / "agent" / "patterns.ndjson"
    valid_ids = set()
    
    if not patterns_file.exists():
        print(f"Warning: {patterns_file} not found")
        return valid_ids
    
    with open(patterns_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                pattern = json.loads(line)
                if "id" in pattern:
                    valid_ids.add(pattern["id"])
                # Also add title-based references (common in markdown)
                if "title" in pattern:
                    valid_ids.add(pattern["title"])
            except json.JSONDecodeError:
                continue
    
    return valid_ids


def extract_pattern_references(content: str) -> list:
    """Extract pattern references from markdown content."""
    patterns = []
    
    # Look for patterns in YAML frontmatter arrays
    yaml_patterns = re.findall(r'patterns:\s*\[(.*?)\]', content, re.DOTALL)
    for match in yaml_patterns:
        # Split by comma and clean up
        for p in match.split(','):
            p = p.strip().strip('"').strip("'")
            if p:
                patterns.append(p)
    
    # Look for patterns in "Related failure patterns:" sections
    # Capture all lines until a blank line or end of string
    related_section = re.search(
        r'\*\*Related failure patterns:\*\*[:\s]*\n((?:(?!\n\n).)*)',
        content,
        re.DOTALL
    )
    if related_section:
        raw_list = related_section.group(1)
        for line in raw_list.split('\n'):
            line = line.strip()
            # Match strict bullet point "- Pattern Name"
            # distinct from "---" separator
            if line.startswith('- ') and not line.startswith('---'):
                pattern_name = line[2:].strip()
                if pattern_name:
                    patterns.append(pattern_name)
    
    return patterns


def validate_patterns(repo_root: Path) -> list:
    """Validate all pattern references in category files."""
    errors = []
    
    valid_patterns = load_valid_pattern_ids(repo_root)
    if not valid_patterns:
        errors.append("No valid patterns found in patterns.ndjson")
        return errors
    
    category_files = [
        "ai-slop-and-automation.md",
        "production-outages.md",
        "security-incidents.md",
        "startup-failures.md",
        "product-failures.md",
        "decision-failures.md",
    ]
    
    for filename in category_files:
        file_path = repo_root / filename
        if not file_path.exists():
            continue
        
        content = file_path.read_text(encoding="utf-8")
        
        # Split by entries (### headers)
        lines = content.split('\n')
        current_entry = []
        entry_title = None
        entry_count = 0
        
        for line in lines:
            if line.startswith('### '):
                # Process previous entry
                if current_entry and entry_title:
                    entry_content = '\n'.join(current_entry)
                    referenced_patterns = extract_pattern_references(entry_content)
                    
                    for pattern in referenced_patterns:
                        # Check against both IDs and titles
                        if pattern not in valid_patterns:
                            # Also check kebab-case version
                            kebab_version = pattern.lower().replace(' ', '-').replace('≠', '-not-')
                            if kebab_version not in valid_patterns:
                                errors.append(
                                    f"{filename}: Entry '{entry_title}' references unknown pattern: '{pattern}'"
                                )
                
                # Start new entry
                entry_title = line[4:].strip()
                current_entry = [line]
                entry_count += 1
            elif entry_title:
                current_entry.append(line)
        
        # Process last entry
        if current_entry and entry_title:
            entry_content = '\n'.join(current_entry)
            referenced_patterns = extract_pattern_references(entry_content)
            
            for pattern in referenced_patterns:
                if pattern not in valid_patterns:
                    kebab_version = pattern.lower().replace(' ', '-').replace('≠', '-not-')
                    if kebab_version not in valid_patterns:
                        errors.append(
                            f"{filename}: Entry '{entry_title}' references unknown pattern: '{pattern}'"
                        )
    
    return errors


def main():
    """Main validation function."""
    repo_root = Path(__file__).parent.parent
    
    print("Validating pattern references...")
    errors = validate_patterns(repo_root)
    
    if errors:
        print("\nPattern validation failed with the following errors:")
        for error in errors:
            print(f"  - {error}")
        print(f"\nTotal errors: {len(errors)}")
        sys.exit(1)
    else:
        print("All pattern references validated successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
