#!/usr/bin/env python3
"""
Validate markdown entries in the repo.
Checks for:
- Required sections (What happened, Impact, Root cause, Lessons, Source)
- At least 2 lessons listed
- Source URL present and valid format
- Tags present
"""

import re
import sys
from pathlib import Path


def validate_entry(file_path, content):
    """Validate a single entry."""
    errors = []

    # Check for required structure elements
    if "**What happened:**" not in content:
        errors.append(f"Missing '**What happened:**' section")
    if "**Impact:**" not in content:
        errors.append(f"Missing '**Impact:**' section")
    if "**Root cause:**" not in content:
        errors.append(f"Missing '**Root cause:**' section")
    if "**Lessons:**" not in content:
        errors.append(f"Missing '**Lessons:**' section")
    if "**Source:**" not in content:
        errors.append(f"Missing '**Source:**' section")

    # Count lessons (look for bullet points)
    lessons_count = len(re.findall(r"^\s*-\s+", content, re.MULTILINE))
    if lessons_count < 2:
        errors.append(f"Only {lessons_count} lessons found. Minimum 2 required.")

    # Check source URL format
    source_match = re.search(r"\*\*Source:\*\*\s*(https?://[^\s]+)", content)
    if not source_match:
        errors.append(f"Missing or invalid source URL")

    # Check for tags array (at minimum)
    if "tags:" not in content.lower():
        errors.append(f"Missing 'tags:' in entry")

    # Check for evidence-type field (only required for ai-slop entries in ai-slop-and-automation.md)
    if "ai-slop-and-automation.md" in str(file_path):
        if (
            "evidence-type:" not in content.lower()
            and "**Evidence type:**" not in content
        ):
            errors.append(
                f"Missing 'Evidence type:' field (Direct incident or Repeated pattern)"
            )

    return errors


def main():
    """Main validation function."""
    repo_root = Path(__file__).parent.parent
    category_files = [
        "ai-slop-and-automation.md",
        "production-outages.md",
        "security-incidents.md",
        "startup-failures.md",
        "product-failures.md",
        "decision-failures.md",
    ]

    all_errors = []

    for filename in category_files:
        file_path = repo_root / filename
        if not file_path.exists():
            continue

        content = file_path.read_text(encoding="utf-8")

        # Split content by finding ### headers
        # Each entry starts with ### and contains a code block
        lines = content.split("\n")
        current_entry = []
        in_entry = False
        entry_count = 0

        for line in lines:
            if line.startswith("### "):
                # If we were in an entry, validate it
                if in_entry and current_entry:
                    entry_content = "\n".join(current_entry)
                    errors = validate_entry(file_path, entry_content)
                    if errors:
                        all_errors.append(f"\n{filename} (Entry {entry_count}):")
                        for error in errors:
                            all_errors.append(f"  - {error}")
                # Start new entry
                current_entry = [line]
                in_entry = True
                entry_count += 1
            elif in_entry:
                current_entry.append(line)
            elif current_entry:
                # We're not in an entry and we have content - check if it starts an entry
                if "```yaml" in line:
                    # This is actually an entry without a ### header
                    # Put it back and treat as entry
                    current_entry.append(line)
                    in_entry = True
                    entry_count += 1

        # Validate last entry
        if in_entry and current_entry:
            entry_content = "\n".join(current_entry)
            errors = validate_entry(file_path, entry_content)
            if errors:
                all_errors.append(f"\n{filename} (Entry {entry_count}):")
                for error in errors:
                    all_errors.append(f"  - {error}")

    if all_errors:
        print("Validation failed with the following errors:")
        print("".join(all_errors))
        sys.exit(1)
    else:
        print("All entries validated successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
