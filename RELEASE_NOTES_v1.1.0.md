# v1.1.0: The Intelligence Layer 🧠

This release upgrades **Awesome Tech Failures** from a comprehensive dataset into a **connected intelligence graph** distributed as a native package for Python and Node.js.

## 📦 Package Distribution
You can now integrate the failure index directly into your monitoring agents, CI pipelines, or analysis tools.

### Python
```bash
pip install git+https://github.com/rnzor/awesome-tech-failures.git@v1.1.0
```
```python
import awesome_tech_failures as atf

# Access the full graph
entries = atf.load_entries()  # 62 structured failures
graph = atf.load_graph()      # connectivity map
```

### Node.js
```bash
npm install rnzor/awesome-tech-failures
```

## 🕸️ The Connectivity Graph
We've implemented a similarity engine that analyzes failure patterns and tags to generate a weighted semantic graph.
- **Nodes**: 62 Failure Entries
- **Edges**: 219 High-Confidence Links
- **Algorithm**: Weighted Jaccard Similarity ($W_{tags} + W_{patterns}$)

## 📚 Source Registry
To combat link rot, we've introduced `agent/sources.json`, a centralized registry of **101 unique sources** with stable, hash-based IDs.
- **Stable IDs**: `src_1a2b3c4d` reference format.
- **Integrity**: `check_links.py` validation in CI.

## 🚀 Pre-Computed Embeddings
The repository now includes `agent/embeddings.ndjson` (384-dim), enabling **Zero-Shot RAG** for any AI agent without needing an initial indexing pass.

---
*Build safer systems by learning from the interconnected history of failure.*
