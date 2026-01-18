#!/usr/bin/env python3
"""
Validate markdown entries in the repo.
Checks for:
- Valid YAML frontmatter
- Required tags (type, cause, stage, impact)
- Source URL present and valid format
- At least 2 lessons listed
- No obvious markdown formatting errors
"""

import re
import sys
from pathlib import Path
import yaml


REQUIRED_TAGS = ["type", "cause", "stage", "impact"]
VALID_TYPES = ["ai-slop", "outage", "security", "startup", "product", "decision"]
VALID_CAUSES = ["ai", "automation", "architecture", "human-error", "incentives"]
VALID_STAGES = ["early", "growth", "scale", "decline"]
VALID_IMPACTS = ["data-loss", "money", "trust", "users", "morale"]


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not match:
        return None, content
    try:
        frontmatter = yaml.safe_load(match.group(1))
        body = match.group(2)
        return frontmatter, body
    except yaml.YAMLError:
        return None, content


def validate_entry(file_path, content):
    """Validate a single entry."""
    errors = []

    # Check frontmatter
    frontmatter, body = parse_frontmatter(content)
    if frontmatter is None:
        errors.append(f"Missing or invalid YAML frontmatter")
        return errors

    # Check required tags
    for tag in REQUIRED_TAGS:
        if tag not in frontmatter:
            errors.append(f"Missing required tag: {tag}")

    # Validate tag values
    if "type" in frontmatter and frontmatter["type"] not in VALID_TYPES:
        errors.append(
            f"Invalid type: {frontmatter['type']}. Must be one of {VALID_TYPES}"
        )

    if "cause" in frontmatter and frontmatter["cause"] not in VALID_CAUSES:
        errors.append(
            f"Invalid cause: {frontmatter['cause']}. Must be one of {VALID_CAUSES}"
        )

    if "stage" in frontmatter and frontmatter["stage"] not in VALID_STAGES:
        errors.append(
            f"Invalid stage: {frontmatter['stage']}. Must be one of {VALID_STAGES}"
        )

    if "impact" in frontmatter and frontmatter["impact"] not in VALID_IMPACTS:
        errors.append(
            f"Invalid impact: {frontmatter['impact']}. Must be one of {VALID_IMPACTS}"
        )

    # Check for source URL
    if "source" not in frontmatter and "Source" not in frontmatter:
        errors.append("Missing source URL in frontmatter")
    elif "source" in frontmatter and not frontmatter["source"].startswith("http"):
        errors.append(f"Invalid source URL: {frontmatter['source']}")

    # Check for lessons (look for "Lessons:" header)
    if (
        "**Lessons:**" not in body
        and "## Lessons" not in body
        and "Lessons:" not in body
    ):
        errors.append("Missing 'Lessons:' section in entry body")

    # Count lessons (look for bullet points under lessons)
    lessons_count = len(re.findall(r"^\s*-\s+", body))
    if lessons_count < 2:
        errors.append(f"Only {lessons_count} lessons found. Minimum 2 required.")

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

        content = file_path.read_text()

        # Split content into individual entries
        entries = re.split(r"^###\s+", content, flags=re.MULTILINE)

        for i, entry in enumerate(entries[1:]):  # Skip first split (before first ###)
            entry_content = "### " + entry.strip()

            # Skip section headers (entries without frontmatter)
            if "---" not in entry_content:
                continue

            errors = validate_entry(file_path, entry_content[:500] + "...")

            if errors:
                all_errors.append(f"\n{filename} (Entry {i + 1}):")
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
