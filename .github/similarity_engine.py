#!/usr/bin/env python3
"""
Calculates similarity between entries and generates a connectivity graph.
Uses Tag and Pattern overlap.
"""

import json
from pathlib import Path

def jaccard_similarity(set1, set2):
    if not set1 and not set2:
        return 0.0
    u = set1.union(set2)
    if not u:
        return 0.0
    return len(set1.intersection(set2)) / len(u)

def main():
    repo_root = Path(__file__).parent.parent
    entries_file = repo_root / 'agent' / 'entries.ndjson'
    
    if not entries_file.exists():
        print(f"Error: {entries_file} not found")
        return

    entries = []
    with open(entries_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                entries.append(json.loads(line))

    graph = {
        "nodes": [],
        "edges": []
    }

    # Add nodes
    for entry in entries:
        graph["nodes"].append({
            "id": entry["id"],
            "title": entry.get("title", ""),
            "category": entry.get("category", "") or entry.get("type", "")
        })

    # Calculate edges
    # Weight threshold for edges
    THRESHOLD = 0.2

    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            e1 = entries[i]
            e2 = entries[j]
            
            tags1 = set(e1.get("tags", []) or [])
            tags2 = set(e2.get("tags", []) or [])
            
            patterns1 = set(e1.get("patterns", []) or [])
            patterns2 = set(e2.get("patterns", []) or [])
            
            s_tags = jaccard_similarity(tags1, tags2)
            s_patterns = jaccard_similarity(patterns1, patterns2)
            
            # Combined score
            score = (0.5 * s_tags) + (0.5 * s_patterns)
            
            if score >= THRESHOLD:
                graph["edges"].append({
                    "source": e1["id"],
                    "target": e2["id"],
                    "weight": round(score, 3),
                    "tags_overlap": list(tags1.intersection(tags2)),
                    "patterns_overlap": list(patterns1.intersection(patterns2))
                })

    graph_file = repo_root / 'agent' / 'graph.json'
    with open(graph_file, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2)
        
    print(f"Graph generated with {len(graph['nodes'])} nodes and {len(graph['edges'])} edges in {graph_file}")

if __name__ == '__main__':
    main()
