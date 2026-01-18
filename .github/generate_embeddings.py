#!/usr/bin/env python3
"""
Generates deterministic "mock" embeddings for development.
Uses a hash of the text to generate consistent vectors.
In a real environment, replace this with a call to SentenceTransformers or OpenAI.
"""

import json
import hashlib
import struct
from pathlib import Path

def generate_mock_vector(text, dimensions=384):
    """Generate a deterministic vector from text hash."""
    # Seed based on text
    seed_hash = hashlib.sha256(text.encode()).digest()
    
    vector = []
    for i in range(dimensions):
        # Use parts of the hash to generate floats between -1 and 1
        # We rotate the hash to get enough values
        val_hash = hashlib.sha256(seed_hash + struct.pack('<I', i)).digest()
        # Get first 4 bytes as a float
        int_val = struct.unpack('<I', val_hash[:4])[0]
        float_val = (int_val / 4294967295.0) * 2 - 1
        vector.append(round(float_val, 6))
    
    return vector

def main():
    repo_root = Path(__file__).parent.parent
    entries_file = repo_root / 'agent' / 'entries.ndjson'
    
    if not entries_file.exists():
        print(f"Error: {entries_file} not found")
        return

    embeddings = []
    with open(entries_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                entry = json.loads(line)
                
                # Create text to embed
                text = f"{entry.get('title', '')} {entry.get('summary', '')} {' '.join(entry.get('lessons', []))}"
                
                vector = generate_mock_vector(text)
                
                embeddings.append({
                    "id": entry["id"],
                    "model": "mock-all-MiniLM-L6-v2",
                    "dimensions": 384,
                    "vector": vector
                })

    outfile = repo_root / 'agent' / 'embeddings.ndjson'
    with open(outfile, 'w', encoding='utf-8') as f:
        for emb in embeddings:
            f.write(json.dumps(emb) + '\n')
            
    print(f"Successfully generated {len(embeddings)} mock embeddings in {outfile}")
    print("Note: These are deterministic hashv-vectors for testing integration.")

if __name__ == '__main__':
    main()
