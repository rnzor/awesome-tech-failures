# Failure Patterns Index 🧠

This index extracts **recurring failure patterns** across outages, startups, products, security incidents, and AI/automation failures.

Patterns matter more than incidents.
Different systems fail in the same ways.

Each pattern links multiple real failures so you can reason by analogy:
> "This looks familiar — where have we seen this break before?"

---

## 1. Automation Without Reversal

**Description**
Automation or agents are given power without clear rollback, kill-switches, or blast-radius limits.

**Seen in**
- Knight Capital trading incident
- AI agent deleting production data
- CI/CD pipelines pushing bad configs globally

**Why it happens**
- Automation optimized for speed, not safety
- Rollbacks considered "edge cases"
- Humans assume automation is safer than it is

**Lessons**
- Every automated action needs a *cheap undo*
- Kill switches must be faster than execution
- Autonomous ≠ unsupervised

**Common tags**
`automation` `no-rollback` `agent-failure` `blast-radius`

---

## 2. Blind Trust in AI Output ("AI Slop")

**Description**
AI-generated outputs are treated as correct by default and shipped or acted on without verification.

**Seen in**
- AI-generated SEO content tanking traffic
- AI summaries replacing human understanding
- LLM-written code deployed without review

**Why it happens**
- AI output sounds confident
- Time pressure rewards speed over understanding
- People confuse fluency with correctness

**Lessons**
- AI is a generator, not a validator
- Require human review at decision boundaries
- Replace *toil*, not *thinking*

**Common tags**
`ai-slop` `blind-trust` `hallucination-in-prod` `decision-degradation`

---

## 3. Hidden Single Point of Failure

**Description**
A system assumed to be redundant depends on a shared component that silently becomes a global SPOF.

**Seen in**
- AWS us-east-1 S3 outage
- GitHub database replication failure
- Control-plane outages taking down "independent" services

**Why it happens**
- Partial migrations
- Shared control planes
- Logical coupling masked as physical separation

**Lessons**
- Map dependencies explicitly
- Test *absence*, not just failure
- Control planes deserve paranoia

**Common tags**
`architecture` `hidden-dependency` `control-plane` `blast-radius`

---

## 4. Overconfidence From Past Success

**Description**
"We've done this before" replaces active risk assessment.

**Seen in**
- GitHub maintenance causing outage
- Repeated AWS regional failures
- Teams skipping dry-runs or game days

**Why it happens**
- Familiarity breeds complacency
- Success rewrites memory of near-misses
- Risk decays invisibly

**Lessons**
- Past success increases future risk
- Rehearse failure paths regularly
- Institutional memory must be written, not assumed

**Common tags**
`human-error` `complacency` `rollback-failure`

---

## 5. Ecosystem Neglect

**Description**
A technically solid product fails because developers, partners, or users don't adopt it.

**Seen in**
- Windows Phone
- Google Wave
- Multiple internal platform rewrites

**Why it happens**
- Focus on core product over ecosystem
- Underestimating switching costs
- Assuming "they will come"

**Lessons**
- Platforms are social systems
- Developers are customers
- Adoption beats elegance

**Common tags**
`ecosystem-failure` `platform-risk` `wrong-market`

---

## 6. Money ≠ Product-Market Fit

**Description**
Capital and talent are used to compensate for missing demand.

**Seen in**
- Quibi shutdown
- Well-funded startups with no retention
- Enterprise products nobody actually wants

**Why it happens**
- Validation skipped due to confidence
- Distribution assumptions go untested
- Prestige replaces feedback

**Lessons**
- PMF is discovered, not declared
- Distribution is part of the product
- Users vote with behavior, not praise

**Common tags**
`no-pmf` `distribution` `burn-rate`

---

## 7. Misconfigured Trust Boundaries

**Description**
Systems assume internal access is safe.

**Seen in**
- Capital One breach
- Cloud IAM misconfigurations
- Internal tools exposed via SSRF

**Why it happens**
- "Internal" treated as "trusted"
- IAM complexity grows faster than understanding
- Security reviews lag infra changes

**Lessons**
- Zero trust is a mindset, not a product
- Internal access must be hostile by default
- Permissions should decay, not accumulate

**Common tags**
`security` `misconfiguration` `iam` `ssrf`

---

## 8. Decision-Making by Proxy

**Description**
Leaders or teams stop engaging with raw data and rely on summaries, dashboards, or AI outputs.

**Seen in**
- AI summaries replacing analysis
- KPI dashboards hiding real user behavior
- Delegated decision-making without context

**Why it happens**
- Scale increases cognitive load
- Tools promise clarity
- Reading source material feels "slow"

**Lessons**
- Compression removes nuance
- Leaders must touch reality regularly
- Tools support judgment — they don't replace it

**Common tags**
`decision` `ai-slop` `incentive-mismatch`

---

## 9. The Innovator's Dilemma

**Description**
Successful companies with profitable legacy products fail to invest in disruptive alternatives because it threatens current revenue.

**Seen in**
- Kodak invented digital camera, buried it for 20 years
- Blockbuster passed on Netflix
- Nokia dismissed iPhone

**Why it happens**
- Leadership incentives tied to short-term profits
- Fear of cannibalizing successful products
- No ownership of disruptive transition

**Lessons**
- Incentives that reward defending the past will destroy the future
- Innovation requires separate metrics and authority
- Market disruption doesn't wait for comfortable transitions
- Cannibalization fear without action just delays the inevitable

**Common tags**
`incentives` `innovators-dilemma` `fear-of-cannibalization` `missed-opportunity`

---

## 10. Patching Debt

**Description**
Security patches are delayed due to operational complexity, only to be exploited while waiting.

**Seen in**
- Equifax breach (Apache Struts patch delayed 2 months)
- Many other breach postmortems
- Legacy systems that can't be patched without downtime

**Why it happens**
- "Patch would require downtime"
- Complex testing requirements
- Change management overhead

**Lessons**
- Critical patches deployed within 24-48 hours
- Unpatched systems are breach-waiting-to-happen
- Accept that maintenance windows are part of security
- Automated testing pipelines reduce patch friction

**Common tags**
`security` `unpatched` `vulnerability` `change-management`

---

## How to Use This Index

**Humans:**
Before shipping automation, agents, rewrites, or strategy shifts — scan patterns, not incidents.

**AI agents:**
Use patterns as *negative priors*:
"This plan resembles past failures with these tags."

---

## Contributing New Patterns

A pattern should:
- Appear in **multiple categories**
- Explain *why*, not just *what*
- Be reusable across domains (infra, AI, startup, product)

If it only fits one incident, it's not a pattern yet.
