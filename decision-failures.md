# Decision & Process Failures ⚙️

Failures not caused by code, but by how decisions were made.
Incentive misalignment, ownership gaps, and the quiet killers of organizations.

---

## Entry Template

```yaml
---
type: decision
cause: [incentives|no-owner|incentive-mismatch]
stage: [early|growth|scale|decline]
impact: [morale|money|trust]
tags: [free-form, tags]
---

**What happened:** [1-2 lines]

**Impact:** [who/what got hit]

**Root cause:** [best-known explanation]

**Lessons:**
- [Actionable lesson 1]
- [Actionable lesson 2]

**Source:** [URL]
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
---

**What happened:** Kodak engineer Steve Sasson invented the digital camera in 1975. Kodak filed the patent and buried it for 20+ years, afraid it would destroy their film business. Filed for bankruptcy in 2012.

**Impact:** From 90% film market share to bankruptcy; $28B market cap to zero; 140,000 employees to a fraction; the company that invented digital photography lost to companies that didn't invent it.

**Root cause:** Leadership incentives tied to short-term film profits; fear of cannibalization; no ownership of digital transition; "innovator's dilemma" in pure form—success blinded them to disruption.

**Lessons:**
- Incentives that reward defending the past will destroy the future
- Cannibalization fear without action just delays the inevitable
- Innovation requires ownership and metrics separate from legacy business
- Market disruption doesn't wait for comfortable transitions

**Source:** https://quartr.com/insights/edge/the-dilemma-that-brought-down-kodak

**Related failure patterns:**
- The Innovator's Dilemma

```yaml
severity: critical
recurrence: single
prevention: Separate innovation metrics from legacy business metrics; create competing internal units
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
---

**What happened:** Teams across multiple organizations began relying on AI-generated summaries instead of reading source data, leading to cascading bad strategic decisions based on incomplete understanding.

**Impact:** Strategic misprioritization; lost time correcting errors; team morale damage as decisions based on summaries proved wrong; rebuild of trust in data required.

**Root cause:** Delegating thinking, not just toil; AI used to compress data but output treated as authoritative; leaders stopped verifying against sources; "efficiency" prioritized over accuracy.

**Lessons:**
- AI should compress data, not replace judgment
- Leaders must still read the source for critical decisions
- Summary is a starting point, not the endpoint of reasoning
- Verify AI output against source material for high-stakes decisions

**Source:** https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-risk-of-relying-on-ai-summaries

**Related failure patterns:**
- Decision-Making by Proxy

```yaml
severity: high
recurrence: recurring
prevention: Require source verification for strategic decisions; audit AI summary accuracy regularly
```

---

## Incentive Mismatch

## Incentive Mismatch

## Meeting-Driven Development

## Rewrite Fever

## Speed Over Quality
