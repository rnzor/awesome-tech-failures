# Tags Reference

## Required Tags (per entry)

### Type
- `ai-slop` — low-quality AI usage causing real harm
- `outage` — availability/latency incidents
- `security` — breaches, leaks, trust failures
- `startup` — shutdowns, PMF failures, burn issues
- `product` — flops, strategy failures, ecosystem mismatches
- `decision` — process, incentives, leadership, ownership failures

### Primary Cause
- `ai` — model/tool behavior issues
- `automation` — scripts/agents/CI/CD causing harm
- `architecture` — coupling, SPOFs, complexity
- `human-error` — mistakes, fatigue, gaps
- `incentives` — KPIs, politics, misalignment

### Stage
- `early` — pre-PMF, seed to Series A
- `growth` — product-market fit, scaling team
- `scale` — major expansion, Series B+
- `decline` — shrinking, pivot, shutdown

### Impact
- `data-loss` — permanent or significant data destruction
- `money` — direct financial loss ($10k+)
- `trust` — brand/reputational damage
- `users` — user impact (churn, complaints, support volume)
- `morale` — team impact (burnout, departures)

---

## Free Tags (examples by category)

### AI Slop / Agent Risks
- `blind-trust` — over-relying on AI output without verification
- `hallucination-in-prod` — model-generated false info shipped
- `prompt-injection` — adversarial input manipulating behavior
- `tool-misuse` — using AI for tasks it wasn't designed for
- `over-automation` — removing human oversight where needed
- `runaway-costs` — agent loops, token explosion
- `no-guardrails` — missing limits on AI actions
- `no-human-in-loop` — autonomous decisions without approval
- `bad-evals` — inadequate testing/evaluation of AI systems
- `vibe-coding` — shipping code without understanding
- `ai-summary-replacement` — using summaries instead of reading source

### Production / Infra Patterns
- `blast-radius` — failure affecting large portion of users
- `hidden-dependency` — undocumented or implicit coupling
- `control-plane` — management/coordination layer failure
- `rollback-failure` — couldn't revert to known-good state
- `observability-gap` — couldn't detect or diagnose issue
- `capacity` — resource exhaustion, throttling, cascading failures
- `cascading-failure` — one failure triggering others
- `single-point-of-failure` — lack of redundancy

### Security Patterns
- `breach` — unauthorized access to systems/data
- `misconfiguration` — incorrect security settings
- `supply-chain` — compromised dependency or vendor
- `auth` — authentication/authorization failures
- `human-factor` — social engineering, credential theft
- `data-exposure` — sensitive data publicly accessible
- `privilege-escalation` — gaining unauthorized permissions

### Startup Patterns
- `no-pmf` — product didn't solve real user problem
- `distribution` — couldn't reach customers effectively
- `pricing` — revenue model issues
- `founder-conflict` — leadership breakdown
- `burn-rate` — spending exceeded runway
- `premature-scale` — growing before ready
- `technical-debt` — accumulated shortcuts causing problems

### Product / Strategy Patterns
- `timing` — too early, too late, or wrong market
- `ecosystem` — dependency on external platform changes
- `ux-mismatch` — product didn't match user mental models
- `platform-risk` — over-reliance on single platform
- `feature-creep` — too many features, diluted value
- `competition` — outmaneuvered by competitors

### Decision / Process Patterns
- `no-owner` — unclear responsibility
- `incentive-mismatch` — wrong KPIs driving behavior
- `meeting-driven-dev` — decisions made in meetings, not code
- `rewrite-fever` — constant rewrites instead of iteration
- `speed-over-quality` — shipping fast, breaking things
- `silo-effect` — teams not sharing information
- `groupthink` — no dissenting views on decisions
- `metrics-gaming` — optimizing metrics, not outcomes

---

## Tagging Guidelines

1. **At minimum**: every entry needs type, cause, stage, impact
2. **Free tags**: add 2-5 relevant tags from above or create new ones
3. **Be consistent**: if a pattern appears in multiple entries, use the same tag
4. **AI agents**: tags enable RAG retrieval and pattern matching
5. **Searchability**: well-tagged entries help both humans and AI find relevant failures
