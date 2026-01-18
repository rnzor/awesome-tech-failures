#!/usr/bin/env python3
"""
Check for missing archive URLs in entries.ndjson.
Warns about sources without Wayback Machine archive links.
Does not fail the build - just provides informational output.
"""

import json
import sys
from pathlib import Path

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def check_wayback_availability(url: str) -> str | None:
    """Check if URL is archived on Wayback Machine. Returns archive URL or None."""
    if not HAS_REQUESTS:
        return None
    try:
        resp = requests.get(
            f"https://archive.org/wayback/available?url={url}",
            timeout=10
        )
        data = resp.json()
        snapshots = data.get("archived_snapshots", {})
        closest = snapshots.get("closest", {})
        return closest.get("url")
    except Exception:
        return None


def main():
    repo_root = Path(__file__).parent.parent
    entries_file = repo_root / "agent" / "entries.ndjson"

    if not entries_file.exists():
        print(f"Error: {entries_file} not found")
        sys.exit(1)

    missing_archives = []
    total_sources = 0
    entries_checked = 0

    with open(entries_file, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            entries_checked += 1
            entry_id = entry.get("id", f"line-{line_num}")
            sources = entry.get("sources", [])
            
            # Handle both array of strings and array of objects
            for idx, src in enumerate(sources):
                total_sources += 1
                if isinstance(src, str):
                    url = src
                    has_archive = False
                elif isinstance(src, dict):
                    url = src.get("url", "")
                    has_archive = bool(src.get("archive_url"))
                else:
                    continue

                if url and not has_archive:
                    missing_archives.append({
                        "entry_id": entry_id,
                        "source_idx": idx,
                        "url": url
                    })

    print(f"📊 Archive Coverage Report")
    print(f"   Entries checked: {entries_checked}")
    print(f"   Total sources: {total_sources}")
    print(f"   Missing archives: {len(missing_archives)}")
    print()

    if missing_archives:
        coverage = ((total_sources - len(missing_archives)) / total_sources * 100) if total_sources > 0 else 0
        print(f"⚠️  Archive coverage: {coverage:.1f}%")
        print()
        print("Sources without archive URLs (first 15):")
        for item in missing_archives[:15]:
            print(f"  - [{item['entry_id']}] {item['url'][:60]}...")
        if len(missing_archives) > 15:
            print(f"  ... and {len(missing_archives) - 15} more")
        
        print()
        print("💡 TIP: Add Wayback Machine archive URLs to prevent link rot.")
        print("   Format: https://web.archive.org/web/YYYYMMDD/original-url")
        print()
        # Don't fail the build, just warn
        sys.exit(0)
    else:
        print(f"✅ All {total_sources} sources have archive URLs!")
        sys.exit(0)


if __name__ == "__main__":
    main()
