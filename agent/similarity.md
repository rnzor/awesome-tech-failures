# Failure Similarity Algorithm Spec 🧮

This document defines the algorithm used to calculate the "Similarity Score" between a user's proposed plan (or an active incident) and our database of failure entries.

---

## 1. Algorithm Overview

The similarity score $S$ (0.0 to 1.0) is a weighted composite of four factors:

$$ S = (W_t \cdot S_{tags}) + (W_p \cdot S_{patterns}) + (W_c \cdot S_{context}) + (W_s \cdot S_{semantic}) $$

Where:
- $S_{tags}$: Jaccard similarity of tags
- $S_{patterns}$: Overlap of fundamental failure patterns
- $S_{context}$: Matches in stage, stack, or category
- $S_{semantic}$: Vector embedding cosine similarity

Default Weights:
- $W_t = 0.3$ (Tags are high signal)
- $W_p = 0.3$ (Patterns are critical architecture matches)
- $W_c = 0.1$ (Context ensures domain relevance)
- $W_s = 0.3$ (Semantic captures un-tagged nuance)

---

## 2. Component Definitions

### A. Tag Similarity ($S_{tags}$)
$$ S_{tags} = \frac{|T_{input} \cap T_{entry}|}{|T_{input} \cup T_{entry}|} $$
*Bonus:* If `critical` tags (e.g., "no-rollback", "blind-trust") match, boost score by +0.1.

### B. Pattern Overlap ($S_{patterns}$)
Binary check. If the input plan triggers the same *Failure Pattern* (e.g., "Automation Without Reversal") as an entry:
$$ S_{patterns} = 1.0 \text{ (if match)} $$
$$ S_{patterns} = 0.0 \text{ (if no match)} $$

### C. Context Match ($S_{context}$)
- **Category Match:** +0.5 (e.g., Input is "AI Agent", Entry is "ai-slop")
- **Stage Match:** +0.3 (e.g., "Scale")
- **Keywords:** +0.2 (e.g., "Postgres", "AWS", "S3")

### D. Semantic Similarity ($S_{semantic}$)
Cosine similarity between the embedding vector of the input description and the entry summary.
$$ S_{semantic} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|} $$

---

## 3. Thresholds & Actions

| Score ($S$) | Risk Level | Action for Agent |
|:---|:---|:---|
| **0.85 - 1.0** | 🔴 **Critical Match** | **BLOCK** execution. Require human override. Show exact failure case. |
| **0.65 - 0.84** | 🟠 **High Risk** | **WARN** user. detailed comparison. Recommend specific guardrails. |
| **0.40 - 0.64** | 🟡 **Medium Risk** | **INFO**. "This reminds me of X." Suggest reviewing playbooks. |
| **< 0.40** | 🔵 **Low Risk** | No proactive alert. Log for audit only. |

---

## 4. Implementation Example (Python-ish)

```python
def calculate_similarity(plan, entry):
    # 1. Tags
    input_tags = extract_tags(plan)
    tag_score = jaccard(input_tags, entry.tags)
    
    # 2. Patterns
    pattern_score = 1.0 if has_common_pattern(plan, entry) else 0.0
    
    # 3. Context
    context_score = 0.0
    if plan.category == entry.category: context_score += 0.5
    if plan.stage == entry.stage: context_score += 0.3
    
    # 4. Semantic (Vector DB lookup)
    semantic_score = vector_db.similarity(plan.embedding, entry.embedding)
    
    # Composite
    final_score = (0.3 * tag_score) + \
                  (0.3 * pattern_score) + \
                  (0.1 * context_score) + \
                  (0.3 * semantic_score)
                  
    return min(final_score, 1.0)
```
