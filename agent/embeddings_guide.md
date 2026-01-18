# Embeddings & RAG Integration Guide 🧠

This guide explains how to integrate the Awesome Tech Failures data into your AI application using embeddings and Retrieval-Augmented Generation (RAG).

---

## 1. Data Sources

| File | Purpose | Format |
|------|---------|--------|
| `agent/entries.ndjson` | All failure entries | Newline-delimited JSON |
| `agent/patterns.ndjson` | All failure patterns | Newline-delimited JSON |
| `agent/tags.json` | Canonical tag definitions | JSON |

---

## 2. Recommended Chunking Strategy

For optimal retrieval, chunk each entry into **two semantic units**:

### Chunk A: Summary + Context
```json
{
  "chunk_type": "summary",
  "entry_id": "aws-s3-us-east-1-2017",
  "text": "AWS S3 us-east-1 Outage (2017). A typo during debugging commands took down S3 in the us-east-1 region, cascading into major internet outages. Root cause: Human error during debugging, insufficient blast-radius controls. Severity: Critical.",
  "metadata": {
    "category": "outage",
    "cause": "human-error",
    "severity": "critical",
    "tags": ["blast-radius", "control-plane", "s3"]
  }
}
```

### Chunk B: Lessons + Patterns
```json
{
  "chunk_type": "lessons",
  "entry_id": "aws-s3-us-east-1-2017",
  "text": "Lessons: Highly available does not mean invulnerable. Region-level dependencies are silent killers. Debugging in production requires extreme caution. Related patterns: Hidden Single Point of Failure, Automation Without Reversal.",
  "metadata": {
    "patterns": ["hidden-single-point-of-failure", "automation-without-reversal"]
  }
}
```

---

## 3. Embedding Model Recommendations

| Use Case | Model | Notes |
|----------|-------|-------|
| **General Purpose** | `text-embedding-3-small` | Good balance of cost and quality |
| **High Quality** | `text-embedding-3-large` | Best for production RAG systems |
| **Open Source** | `nomic-embed-text-v1.5` | Self-hostable, 8192 context |
| **Lightweight** | `all-MiniLM-L6-v2` | Fast, good for prototyping |

---

## 4. Retrieval Strategies

### Strategy 1: Semantic Search
Standard cosine similarity search against user query.

```python
# Pseudocode
query = "What can go wrong with AI agents?"
results = vector_store.similarity_search(query, k=5)
```

### Strategy 2: Hybrid Search (Recommended)
Combine semantic search with tag-based filtering.

```python
# Pseudocode
query = "What can go wrong with AI agents?"
filter = {"category": "ai-slop", "severity": {"$in": ["critical", "high"]}}
results = vector_store.similarity_search(query, k=5, filter=filter)
```

### Strategy 3: Pattern-First Retrieval
First identify matching patterns, then retrieve related entries.

```python
# Pseudocode
patterns = pattern_store.similarity_search("automation without rollback", k=2)
entry_ids = [p.metadata["examples"] for p in patterns]
entries = entry_store.get_by_ids(entry_ids)
```

---

## 5. Context Window Considerations

| Model | Context Window | Recommendation |
|-------|----------------|----------------|
| GPT-4o | 128K | Include 10-15 full entries |
| Claude 3.5 | 200K | Include 20+ full entries |
| Gemini 2.0 | 2M | Include entire dataset if needed |

For smaller context windows, prioritize:
1. Entries matching the user's **category** (ai-slop, outage, security)
2. Entries with **Critical** or **High** severity
3. Entries with overlapping **tags**

---

## 6. Example: Pre-Flight Check RAG Pipeline

```python
def check_plan_against_failures(plan_description: str):
    """
    Given a user's plan (e.g., 'Deploy an AI agent with DB write access'),
    retrieve relevant failure patterns and generate warnings.
    """
    # Step 1: Retrieve relevant entries
    entries = vector_store.similarity_search(plan_description, k=5)
    
    # Step 2: Extract patterns
    patterns = set()
    for entry in entries:
        patterns.update(entry.metadata.get("patterns", []))
    
    # Step 3: Generate risk memo
    prompt = f"""
    The user is planning: {plan_description}
    
    Relevant past failures:
    {format_entries(entries)}
    
    Matching failure patterns: {list(patterns)}
    
    Generate a risk memo with:
    1. Specific warnings based on past failures
    2. Recommended safeguards
    3. Pre-flight checklist items to verify
    """
    return llm.generate(prompt)
```

---

## 7. Keeping Embeddings Updated

When new entries are added to `entries.ndjson`:
1. Parse the new entries
2. Chunk them using the strategy above
3. Generate embeddings
4. Upsert into your vector store

Consider using the `year` and `id` fields as unique identifiers to avoid duplicates.
