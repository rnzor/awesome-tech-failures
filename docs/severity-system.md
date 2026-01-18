# Severity & Risk Scoring System ⚖️

To maintain a "best-in-class" failure repository, we use a standardized scoring system for every entry. This helps humans and AI agents prioritize lessons and understand the true cost of failure.

---

## 1. Severity Levels

We categorize failures into four primary levels based on their maximum impact:

| Level | Definition | Financial Impact | User Impact |
|:---|:---|:---|:---|
| 🔴 **Critical** | Existential threat to the company or global infrastructure. | $10M+ | Millions |
| 🟠 **High** | Significant revenue loss or massive data breach. | $1M - $10M | Hundreds of thousands |
| 🟡 **Medium** | Notable disruption or user trust damage. | $100K - $1M | Thousands |
| 🔵 **Low** | Operational friction or localized incidents. | < $100K | Internal / hundreds |

---

## 2. Risk Dimensions

Each failure is rated on a 1-5 scale across three dimensions:

- **Impact (I):** How much damage was done?
- **Preventability (P):** How easy would it have been to stop this with industry-standard practices?
- **Relevance (R):** How common is this failure pattern in modern (2025+) systems?

**Composite Risk Score:** `(I + P + R) / 3`

---

## 3. Metadata Schema

Every new entry should include a `severity` object in its frontmatter:

```yaml
severity:
  level: critical | high | medium | low
  score: 1-10 (optional)
  financial: "$X"
  user_impact: "high"
```

---

## 4. Why this matters for AI Agents

By providing structured severity data, AI agents can:
1. **Filter by risk:** "Show me all critical AI-slop failures."
2. **Prioritize training:** Weight "Critical" lessons more heavily in RAG-based advice.
3. **Warn users:** "Your proposed architecture matches a 'High' severity failure pattern seen in AWS S3 (2017)."
