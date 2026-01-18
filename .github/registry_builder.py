#!/usr/bin/env python3
"""
Builds a source registry from markdown entries.
Deduplicates URLs and assigns stable IDs.
"""

import json
import re
import hashlib
import yaml
from pathlib import Path

def generate_source_id(url):
    """Generate a stable 8-character ID from a URL hash."""
    return f"src_{hashlib.md5(url.encode()).hexdigest()[:8]}"

def extract_urls(content):
    """Extract URLs from markdown content."""
    # Find all http/https links
    return re.findall(r'https?://[^\s\)\]\"\'\>]+', content)

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

    registry = {}
    
    # First pass: Collect all sources
    for filename in category_files:
        file_path = repo_root / filename
        if not file_path.exists():
            continue
            
        content = file_path.read_text(encoding='utf-8')
        
        # Split by entries (###)
        entries = content.split('### ')
        for entry in entries[1:]: # Skip file header
            # Extract YAML block
            yaml_match = re.search(r'```yaml\s*\n---\s*\n(.*?)\n---\s*\n', entry, re.DOTALL)
            if yaml_match:
                try:
                    data = yaml.safe_load(yaml_match.group(1))
                    if 'sources' in data:
                        source_list = data['sources']
                        if isinstance(source_list, list):
                            for url in source_list:
                                if isinstance(url, str) and url.startswith('http'):
                                    sid = generate_source_id(url)
                                    if sid not in registry:
                                        registry[sid] = {
                                            "url": url,
                                            "status": "active"
                                        }
                except Exception as e:
                    print(f"Error parsing YAML in {filename}: {e}")

            # Also scan body for URLs in 'Source:' or 'Sources:' lines or just any http links
            body_urls = extract_urls(entry)
            for url in body_urls:
                sid = generate_source_id(url)
                if sid not in registry:
                    registry[sid] = {
                        "url": url,
                        "status": "active"
                    }

    # Save Registry
    registry_file = repo_root / 'agent' / 'sources.json'
    with open(registry_file, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2)
        
    print(f"Successfully indexed {len(registry)} unique sources in {registry_file}")

if __name__ == '__main__':
    main()
