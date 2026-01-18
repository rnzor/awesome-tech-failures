#!/usr/bin/env python3
"""
Checks the source registry for broken links.
Performs HEAD requests to verify URL availability.
"""

import json
import urllib.request
import urllib.error
from pathlib import Path

def check_link(url):
    """Perform a HEAD request to check if a link is alive."""
    try:
        # User-Agent to avoid simple bot blocks
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except urllib.error.HTTPError as e:
        # Some sites block HEAD, try GET with small range
        if e.code in [403, 405]:
            try:
                req = urllib.request.Request(url, method='GET', headers={'User-Agent': 'Mozilla/5.0', 'Range': 'bytes=0-0'})
                with urllib.request.urlopen(req, timeout=5) as response:
                    return response.status in [200, 206]
            except:
                return False
        return False
    except:
        return False

def main():
    repo_root = Path(__file__).parent.parent
    registry_file = repo_root / 'agent' / 'sources.json'
    
    if not registry_file.exists():
        print("Error: Registry not found")
        return

    with open(registry_file, 'r', encoding='utf-8') as f:
        registry = json.load(f)

    print(f"Checking {len(registry)} sources for link rot...")
    
    broken_count = 0
    # For this demo, we'll only check a subset to avoid flooding or timeouts
    # In a full CI run, you'd check all.
    limit = 10
    count = 0
    
    for sid, info in registry.items():
        if count >= limit:
            break
        
        url = info['url']
        print(f"Checking [{sid}]: {url} ...", end=" ", flush=True)
        
        if check_link(url):
            print("OK")
            info['status'] = 'active'
        else:
            print("BROKEN")
            info['status'] = 'broken'
            broken_count += 1
            
        count += 1

    # Save updated registry
    with open(registry_file, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2)

    print(f"\nAudit complete. Broken links in subset: {broken_count}")

if __name__ == '__main__':
    main()
