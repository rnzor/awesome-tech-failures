# Startup Failures 🚀

Shutdowns, runways exhausted, product-market fit misses, and the postmortems
from founders who lived to tell the tale.

---

## Entry Template

```yaml
---
type: startup
cause: [incentives|no-pmf|architecture]
stage: [early|growth|scale|decline]
impact: [money|trust|morale]
tags: [free-form, tags]
evidence-type: [direct-incident|repeated-pattern]
severity:
  level: [critical|high|medium|low]
  score: [1-10]
  financial: [Description or N/A]
sources:
  - https://...
supporting-entities: [Entity1, Entity2]
---

**What happened:** [1-2 lines describing the incident]

**Impact:** [who/what got hit]

**Root cause:** [best-known explanation]

**Lessons:**
- [Actionable lesson 1]
- [Actionable lesson 2]

**Related failure patterns:**
- [Pattern 1]
- [Pattern 2]
```

---

## PMF Failures

### (2020) Quibi — $1.75B Burn in 6 Months

```yaml
---
type: startup
cause: incentives
stage: growth
impact: money
tags: [no-pmf, timing, distribution, wrong-assumptions, premium-content]
evidence-type: direct-incident
sources:
  - https://www.theinformation.com/articles/quibi-the-rise-and-fall-of-a-1-75-billion-failure
supporting-entities: [Quibi, The Information]
---

**What happened:** Quibi raised $1.75B to build "Netflix for your phone" with premium short-form content. Launched April 2020, shut down October 2020. Burned through nearly $2B in under 7 months.

**Impact:** Company closed; investors wiped; 500+ employees laid off; content library sold for scraps; became definitive case study in PMF failure.

**Root cause:** No product-market fit; fundamentally wrong assumptions about mobile viewing habits; content didn't justify subscription; premium positioning meaningless without habit formation; distribution strategy failed.

**Lessons:**
- Money doesn't buy demand
- "Premium" means nothing without habit
- Timing assumptions must be tested, not assumed
- Content differentiation must be obvious, not explained

**Related failure patterns:**
- Money ≠ Product-Market Fit
```

---

## Burn Rate & Runway

## Founder Conflict

## Distribution Failures

## Premature Scaling
