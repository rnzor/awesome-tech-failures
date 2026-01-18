# Decision & Process Failures ⚙️

Failures not caused by code, but by how decisions were made.
Incentive misalignment, ownership gaps, and the quiet killers of organizations.

---

## Entry Template

```yaml
---
type: decision
cause: [incentives|no-owner|ai]
stage: [early|growth|scale|decline]
impact: [morale|money|trust]
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

## Innovator's Dilemma

### (1975-2012) Kodak — Invented Digital, Buried It

```yaml
---
type: decision
cause: incentives
stage: scale
impact: money
tags: [innovators-dilemma, fear-of-cannibalization, short-term-incentives, missed-opportunity]
evidence-type: direct-incident
sources:
  - https://quartr.com/insights/edge/the-dilemma-that-brought-down-kodak
supporting-entities: [Kodak]
---

**What happened:** Kodak engineer Steve Sasson invented the digital camera in 1975. Kodak filed the patent and buried it for 20+ years, afraid it would destroy their film business. Filed for bankruptcy in 2012.

**Impact:** From 90% film market share to bankruptcy; $28B market cap to zero; 140,000 employees to a fraction; the company that invented digital photography lost to companies that didn't invent it.

**Root cause:** Leadership incentives tied to short-term film profits; fear of cannibalization; no ownership of digital transition; "innovator's dilemma" in pure form—success blinded them to disruption.

**Lessons:**
- Incentives that reward defending the past will destroy the future
- Cannibalization fear without action just delays the inevitable
- Innovation requires ownership and metrics separate from legacy business
- Market disruption doesn't wait for comfortable transitions

**Related failure patterns:**
- The Innovator's Dilemma
```

---

## No Ownership

### (Ongoing) AI Summaries Replaced Understanding

```yaml
---
type: decision
cause: ai
stage: scale
impact: morale
tags: [blind-trust, decision-degradation, ai-slop, delegation-thinking, leadership-failure]
evidence-type: repeated-pattern
sources:
  - https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-risk-of-relying-on-ai-summaries
supporting-entities: [McKinsey, Various Organizations]
---

**What happened:** Teams across multiple organizations began relying on AI-generated summaries instead of reading source data, leading to cascading bad strategic decisions based on incomplete understanding.

**Impact:** Strategic misprioritization; lost time correcting errors; team morale damage as decisions based on summaries proved wrong; rebuild of trust in data required.

**Root cause:** Delegating thinking, not just toil; AI used to compress data but output treated as authoritative; leaders stopped verifying against sources; "efficiency" prioritized over accuracy.

**Lessons:**
- AI should compress data, not replace judgment
- Leaders must still read the source for critical decisions
- Summary is a starting point, not the endpoint of reasoning
- Verify AI output against source material for high-stakes decisions

**Related failure patterns:**
- Decision-Making by Proxy
```

---

### (2026) AI Pilots Fail Due to Integration Complexity

```yaml
---
type: decision
cause: incentives
stage: scale
impact: [money, morale]
severity:
  level: high
  score: 8
  financial: Pilot investment losses
tags: [pilot-failure, integration-complexity, scale-failure, legacy-systems, ai-deployment]
evidence-type: repeated-pattern
sources:
  - https://www.linkedin.com/pulse/gemini-3-continually-hallucinates-gaslights-face-rag-errors-jesse-vyete
supporting-entities: [Composio, Various AI Vendors]
---

**What happened:** The "2025 AI Agent Report" via Composio found that AI pilots succeed on curated data but fail to scale due to legacy system friction. Integration complexity is the primary blocker for pilot-to-production transitions.

**Impact:** Teams discouraged by the "pilot-to-production gap" after significant capital investment; wasted resources on pilots that cannot be deployed at scale; delayed digital transformation initiatives.

**Root cause:** 
- Pilots ignore legacy API unreliability during controlled testing
- Data format mismatches that work with small datasets become fatal at production scale
- Lack of infrastructure team involvement in pilot planning
- Success on curated, clean data creates false confidence for production deployment

**Lessons:**
- Include infrastructure teams in the pilot phase from day one
- Test agents on real, messy production data early, not just curated datasets
- Map all integration dependencies before declaring pilot success
- Plan for legacy system friction and edge cases in pilot design
- "Pilot success" on clean data is not predictive of production success

**Related failure patterns:**
- Pilot Failure
- Integration Complexity
- Scale Failure
```

---

## Incentive Mismatch

## Incentive Mismatch

## Meeting-Driven Development

## Rewrite Fever

## Speed Over Quality
