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
- Overconfidence From Past Success
- Decision-Making by Proxy
```

---

## Incentive Mismatch

### (2019) Boeing 737 MAX MCAS — When Safety Became Optional

```yaml
---
type: decision
cause: incentives
stage: scale
impact: [trust, users, money]
tags: [safety-over-profit, regulatory-capture, engineering-override, aviation, certification-failure]
evidence-type: direct-incident
severity:
  level: critical
  score: 10
  financial: $20B+ costs
sources:
  - https://www.congress.gov/116/crpt/hrpt364/CRPT-116hrpt364.pdf
  - https://www.nytimes.com/2019/03/23/business/boeing-737-max-crash.html
supporting-entities: [Boeing, FAA, Congress]
---

**What happened:** Boeing's 737 MAX MCAS system was designed to mask aerodynamic changes from pilots. Two crashes killed 346 people. Congressional investigation revealed Boeing pressured engineers, misled regulators, and prioritized schedule over safety.

**Impact:** 346 deaths; fleet grounded worldwide for 20 months; $20B+ in costs; criminal charges; CEO fired; trust in Boeing and FAA devastated.

**Root cause:** Schedule and cost pressure overrode engineering concerns; regulatory capture allowed self-certification; MCAS was a software patch for a hardware problem; single-sensor design was known risk.

**Lessons:**
- When engineers raise safety concerns, listen or face catastrophic consequences
- Self-certification creates conflicts of interest that can kill
- Software cannot permanently fix hardware design decisions
- "Move fast" cultures are incompatible with safety-critical systems

**Related failure patterns:**
- The Innovator's Dilemma
- Decision-Making by Proxy
```

---

### (2013-2019) Yahoo Acquiring Tumblr — $1.1B to $3M

```yaml
---
type: decision
cause: incentives
stage: decline
impact: [money, trust]
tags: [acquisition-failure, culture-mismatch, content-moderation, valuation-destruction]
evidence-type: direct-incident
severity:
  level: high
  score: 8
  financial: $1.1B to $3M
sources:
  - https://www.wsj.com/articles/verizon-sells-tumblr-to-wordpress-owner-11565627453
  - https://www.theverge.com/2019/8/12/20802639/tumblr-verizon-sold-wordpress-blogging-yahoo
supporting-entities: [Yahoo, Verizon, Automattic, WSJ]
---

**What happened:** Yahoo acquired Tumblr for $1.1B in 2013. After mismanagement, content policy disasters, and user exodus, Verizon sold it to Automattic for $3M in 2019 — a 99.7% loss.

**Impact:** $1.097B value destruction; user base collapsed; became case study in how not to acquire and manage a social platform.

**Root cause:** Yahoo didn't understand Tumblr's culture; content moderation decisions alienated core users; advertising strategy failed; NSFW ban killed differentiator.

**Lessons:**
- Acquiring a community means acquiring a culture — don't break it
- Content moderation decisions are product decisions with business consequences
- Paying premium price requires premium execution
- What makes a platform unique is often what acquirers want to remove

**Related failure patterns:**
- Decision-Making by Proxy
- Ecosystem Neglect
```

---

### (2007-2013) Nokia Ignoring iPhone — The Fall of a Giant

```yaml
---
type: decision
cause: incentives
stage: decline
impact: [money, users, trust]
tags: [innovators-dilemma, smartphone, platform-transition, symbian, organizational-inertia]
evidence-type: direct-incident
severity:
  level: critical
  score: 10
  financial: $250B+ market cap loss
sources:
  - https://knowledge.insead.edu/strategy/nokias-fall-grace
  - https://hbr.org/2010/07/how-nokia-lost-the-smartphone
supporting-entities: [Nokia, INSEAD, HBR]
---

**What happened:** Nokia was the world's largest phone maker in 2007. Despite seeing the iPhone threat, organizational inertia and Symbian investment prevented response. Sold mobile division to Microsoft in 2013 for $7.2B.

**Impact:** From 50% smartphone market share to near-zero; $250B+ market cap destruction; 40,000+ employees affected; became textbook case of disruption.

**Root cause:** Middle management fear culture prevented bad news from reaching leadership; Symbian investment created sunk cost fallacy; hardware mindset couldn't adapt to software-defined future.

**Lessons:**
- Fear cultures filter information until it's too late
- Installed base can become an anchor, not an asset
- Platform transitions require burning boats, not hedging
- The innovator's dilemma is real — you can see disruption and still fail

**Related failure patterns:**
- The Innovator's Dilemma
- Overconfidence From Past Success
```

---

### (2000) Blockbuster Passing on Netflix — $50M Decision, $100B Cost

```yaml
---
type: decision
cause: incentives
stage: scale
impact: [money, trust]
tags: [disruption, wrong-assumptions, franchise-model, streaming, late-fee-dependency]
evidence-type: direct-incident
severity:
  level: critical
  score: 9
  financial: Bankruptcy
sources:
  - https://www.inc.com/minda-zetlin/netflix-blockbuster-meeting-marc-randolph-reed-hastings-john-antioco.html
  - https://www.businessinsider.com/blockbuster-ceo-passed-up-chance-to-buy-netflix-for-50-million-2015-7
supporting-entities: [Blockbuster, Netflix, Inc, Business Insider]
---

**What happened:** In 2000, Netflix offered to sell to Blockbuster for $50M. Blockbuster declined, calling it "a very small niche business." Blockbuster filed for bankruptcy in 2010; Netflix is now worth $250B+.

**Impact:** Blockbuster bankruptcy; 9,000 stores closed; 60,000+ jobs lost; Netflix became streaming giant; became defining example of disruption blindness.

**Root cause:** Revenue model dependent on late fees (which Netflix eliminated); franchise owners opposed online shift; couldn't imagine customers preferring convenience over stores.

**Lessons:**
- The threat that seems "too small to matter" is the one that kills you
- Business models built on customer pain (late fees) are disruption targets
- Franchise models resist cannibalization even when necessary for survival
- Never evaluate disruptors by current size, evaluate by trajectory

**Related failure patterns:**
- The Innovator's Dilemma
- Overconfidence From Past Success
```

---

## Meeting-Driven Development

## Rewrite Fever

## Speed Over Quality
