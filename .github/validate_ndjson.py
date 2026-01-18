#!/usr/bin/env python3
"""
Validate agent/entries.ndjson against agent/schema.json.
Runs on every PR to ensure data integrity.
"""

import json
import sys
from pathlib import Path

# Handle Windows encoding issues
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

try:
    from jsonschema import validate, ValidationError
except ImportError:
    print("Error: jsonschema not installed. Run: pip install jsonschema")
    sys.exit(1)


def main():
    repo_root = Path(__file__).parent.parent
    schema_file = repo_root / "agent" / "schema.json"
    entries_file = repo_root / "agent" / "entries.ndjson"

    if not schema_file.exists():
        print(f"Error: Schema file not found: {schema_file}")
        sys.exit(1)

    if not entries_file.exists():
        print(f"Error: Entries file not found: {entries_file}")
        sys.exit(1)

    with open(schema_file, "r", encoding="utf-8") as f:
        schema = json.load(f)

    errors = []
    line_count = 0

    with open(entries_file, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            line_count += 1

            try:
                entry = json.loads(line)
            except json.JSONDecodeError as e:
                errors.append(f"Line {line_num}: Invalid JSON - {e}")
                continue

            try:
                validate(instance=entry, schema=schema)
            except ValidationError as e:
                entry_id = entry.get("id", "unknown")
                # Truncate long error messages for readability
                msg = e.message[:100] + "..." if len(e.message) > 100 else e.message
                errors.append(f"Line {line_num} ({entry_id}): {msg}")

    if errors:
        print(f"[X] Validation failed with {len(errors)} error(s):")
        print()
        for err in errors[:20]:  # Show first 20 errors
            print(f"  - {err}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors")
        print()
        print("TIP: Ensure entries.ndjson fields match schema.json requirements.")
        sys.exit(1)
    else:
        print(f"[OK] All {line_count} entries validated successfully against schema!")
        sys.exit(0)


if __name__ == "__main__":
    main()

