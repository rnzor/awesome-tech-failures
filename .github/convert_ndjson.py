#!/usr/bin/env python3
"""
Build static API - Convert NDJSON to JSON arrays
"""

import json
from pathlib import Path
import sys


def main():
    repo_root = Path(__file__).parent.parent
    agent_dir = repo_root / "agent"
    api_dir = repo_root / "docs" / "api"

    print("Converting NDJSON to JSON arrays...")

    # Create api directory
    api_dir.mkdir(parents=True, exist_ok=True)

    # Convert entries.ndjson → failures.json
    print("Converting entries.ndjson...")
    entries_file = agent_dir / "entries.ndjson"
    output_file = api_dir / "failures.json"
    entries = []
    with open(entries_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                entries.append(json.loads(line))
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)
    print(f"Converted {len(entries)} entries to failures.json")

    # Convert patterns.ndjson → patterns.json
    print("Converting patterns.ndjson...")
    patterns_file = agent_dir / "patterns.ndjson"
    output_file = api_dir / "patterns.json"
    patterns = []
    with open(patterns_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                patterns.append(json.loads(line))
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(patterns, f, indent=2)
    print(f"Converted {len(patterns)} patterns to patterns.json")

    # Convert playbooks.ndjson → playbooks.json
    print("Converting playbooks.ndjson...")
    playbooks_file = agent_dir / "playbooks.ndjson"
    output_file = api_dir / "playbooks.json"
    playbooks = []
    with open(playbooks_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                playbooks.append(json.loads(line))
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(playbooks, f, indent=2)
    print(f"Converted {len(playbooks)} playbooks to playbooks.json")

    print("NDJSON conversion complete!")


if __name__ == "__main__":
    main()
