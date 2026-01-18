# Failure Patterns Index 🧩

Cross-category patterns that appear repeatedly across failures.
Use this index to find similar failures and learn from the patterns.

---

## Pattern: Automation Without Reversibility

**Definition:** Deploying automation (scripts, agents, CI/CD, AI) without the ability to quickly reverse course when things go wrong.

**Appears in:**
- Cloudflare 2019 (regex deployment without rollback testing)
- AI agent runaway scenarios
- CI/CD pipeline failures without rollback

**Risk Indicators:**
- "It will only take a day to deploy"
- "If it breaks, we'll fix it"
- No rollback procedure documented

**Prevention:**
- Every automated deployment must have a tested rollback
- Time-bound canaries with automatic rollback triggers
- Maintain "last known good" state at all times

---

## Pattern: The Innovator's Dilemma

**Definition:** Established companies with successful products fail to invest in disruptive alternatives because it threatens their current revenue.

**Appears in:**
- Kodak (invented digital camera, buried it)
- Blockbuster (passed on Netflix)
- Nokia (dismissed iPhone)

**Risk Indicators:**
- "Our core product is doing great"
- "This new thing won't affect us"
- Innovation teams lack real authority

**Prevention:**
- Separate innovation metrics from legacy metrics
- Give disruptive projects real budget and authority
- Incentivize cannibalization

---

## Pattern: Blind Trust in AI

**Definition:** Treating AI output as authoritative without verification, especially for high-stakes decisions.

**Appears in:**
- Microsoft Tay (trusted user input to train without filtering)
- AI summarization replacing source reading
- AI-generated content without human review

**Risk Indicators:**
- "AI said it, so it must be right"
- No human-in-loop for AI decisions
- Output goes straight to production

**Prevention:**
- AI is always wrong until proven right
- Human review for anything user-facing or high-stakes
- Maintain source of truth; AI is a summary, not the truth

---

## Pattern: Single Points of Failure in Safety Systems

**Definition:** Critical safety mechanisms (circuit breakers, rate limiters, kill switches) are single points of failure themselves.

**Appears in:**
- Cloudflare 2019 (CPU limiter removed "by mistake")
- Any system where safety is maintained by a single component

**Risk Indicators:**
- "This mechanism is so simple it can't fail"
- Safety system not tested regularly
- Changes to safety systems don't require review

**Prevention:**
- Defense in depth for safety systems
- Test safety mechanisms regularly
- Changes to safety systems require signoff

---

## Pattern: Timing Blindness

**Definition:** Building a product for a use case that doesn't exist in the current market context.

**Appears in:**
- Quibi (on-the-go viewing during COVID lockdown)
- Google Glass (AR before social acceptance)
- Any "too early" product

**Risk Indicators:**
- Use case assumes a specific user behavior
- Market conditions have changed recently
- "People will want this eventually"

**Prevention:**
- Test use case assumptions with minimal spend
- Build for current market, not theoretical future market
- Accept that "too early" is the same as "wrong" for startups

---

## Pattern: Patching Debt

**Definition:** Delaying security patches due to operational complexity, only to be exploited.

**Appears in:**
- Equifax 2017 (Apache Struts patch delayed 2 months)
- Many breach postmortems

**Risk Indicators:**
- "Patch would require downtime"
- "We need to test in staging first"
- Patching process takes weeks/months

**Prevention:**
- Critical patches deployed within 24-48 hours
- Automated testing and deployment pipelines
- Accept that unpatched systems are breach-waiting-to-happen

---

## Pattern: The Halo Effect

**Definition:** Over-valuing a team or individual's past success as an indicator of future success.

**Appears in:**
- Quibi (Katzenberg + Whitman = success)
- Many "all-star team" failures

**Risk Indicators:**
- "These people have done it before"
- Less scrutiny on assumptions due to reputation
- Market validation skipped

**Prevention:**
- Past success ≠ future success
- Market validation is mandatory regardless of team
- Apply same rigor to all opportunities

---

## Pattern: Over-Automation

**Definition:** Automating processes that require human judgment or oversight.

**Appears in:**
- AI summary replacing analysis
- Automated customer service without escalation
- Auto-deployment without human approval

**Risk Indicators:**
- "Humans are the bottleneck"
- "The process is straightforward"
- No human review checkpoints

**Prevention:**
- Automate tasks, not decisions
- Maintain human-in-loop for irreversible actions
- Measure automation quality, not just speed

---

## Adding New Patterns

When adding a pattern:
1. Define the pattern clearly (2-3 sentences)
2. List 2-3 real examples from this repo
3. Identify risk indicators (how to spot it coming)
4. Provide prevention strategies (how to avoid it)

Patterns should be actionable and specific, not vague observations.
