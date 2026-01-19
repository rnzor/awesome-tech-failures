#!/usr/bin/env python3
"""
Create hybrid lookup for common terms/patterns.
Pre-computes embeddings for frequently searched terms to avoid API calls.
"""

import json
from pathlib import Path
import hashlib
import struct

# Common terms to pre-embed (expand based on actual usage)
COMMON_TERMS = [
    # AI-related
    "AI agent deployment",
    "automation without rollback",
    "blind trust in AI",
    "LLM failure",
    "multi-agent system",
    "RAG hallucination",
    "prompt injection",
    # Infrastructure
    "database migration",
    "production outage",
    "AWS S3",
    "Cloudflare",
    "Kubernetes",
    # Security
    "data breach",
    "supply chain attack",
    "misconfiguration",
    # Patterns
    "hidden single point of failure",
    "automation without reversal",
    "misconfigured trust boundaries",
    "decision-making by proxy",
]


def generate_mock_vector(text, dimensions=384):
    """Generate deterministic vector from text (same as generate_embeddings.py)."""
    seed_hash = hashlib.sha256(text.encode()).digest()
    vector = []
    for i in range(dimensions):
        val_hash = hashlib.sha256(seed_hash + struct.pack("<I", i)).digest()
        int_val = struct.unpack("<I", val_hash[:4])[0]
        float_val = (int_val / 4294967295.0) * 2 - 1
        vector.append(round(float_val, 6))
    return vector


def main():
    repo_root = Path(__file__).parent.parent
    api_dir = repo_root / "docs" / "api"

    print("Creating hybrid term lookup...")

    hybrid_lookup = {
        "version": "1.0.0",
        "generated_at": "2026-01-19",
        "dimensions": 384,
        "terms": {},
    }

    for term in COMMON_TERMS:
        vector = generate_mock_vector(term)
        hybrid_lookup["terms"][term] = {
            "vector": vector,
            "usage_count": 0,  # Track for future optimization
        }

    # Save to file
    output_file = api_dir / "hybrid_lookup.json"
    with open(output_file, "w") as f:
        json.dump(hybrid_lookup, f, indent=2)

    print(f"Created hybrid lookup with {len(COMMON_TERMS)} terms")
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    main()
