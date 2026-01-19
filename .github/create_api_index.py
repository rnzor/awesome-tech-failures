#!/usr/bin/env python3
"""
Create API index file with metadata and counts.
"""

import json
from pathlib import Path
from datetime import datetime


def main():
    repo_root = Path(__file__).parent.parent
    api_dir = repo_root / "docs" / "api"

    print("Creating API index...")

    # Count entries in each file
    failures_count = len(json.load(open(api_dir / "failures.json")))
    patterns_count = len(json.load(open(api_dir / "patterns.json")))

    # Create index
    api_index = {
        "version": "1.0.0",
        "base_url": "https://rnzor.github.io/awesome-tech-failures/api",
        "generated_at": datetime.now().isoformat(),
        "endpoints": {
            "GET /api/failures": "List all failure entries with optional filtering",
            "GET /api/failures/{id}": "Get specific failure entry by ID",
            "POST /api/search/similarity": "Semantic search with client-side similarity",
            "GET /api/patterns": "List all failure patterns",
            "GET /api/patterns/{id}": "Get specific pattern with related entries",
            "GET /api/tags": "Get tag definitions",
            "GET /api/hybrid_lookup": "Pre-embedded common terms (hybrid mode)",
        },
        "statistics": {
            "failures_count": failures_count,
            "patterns_count": patterns_count,
            "embeddings_available": True,
            "hybrid_mode": True,
        },
        "client_side_features": {
            "similarity_search": {
                "mode": "hybrid",
                "default_implementation": "pre-embedded_terms",
                "optional": "custom_query_embedding_via_api",
            }
        },
    }

    # Save index
    output_file = api_dir / "index.json"
    with open(output_file, "w") as f:
        json.dump(api_index, f, indent=2)

    print(f"✅ Created API index")
    print(f"📊 Statistics: {failures_count} failures, {patterns_count} patterns")
    print(f"📂 Saved to: {output_file}")


if __name__ == "__main__":
    main()
