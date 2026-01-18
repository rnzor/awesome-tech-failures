# Tags Reference

## Required Tags (per entry)

### Type
- `ai-slop` — low-quality AI usage causing real harm
- `outage` — availability/latency incidents
- `security` — breaches, leaks, trust failures
- `startup` — shutdowns, PMF failures, burn issues
- `product` — flops, strategy failures, ecosystem mismatches
- `decision` — process, incentives, leadership, ownership failures

### When to Use `ai-slop`
- Entry is specifically about low-quality AI output causing harm
- Use alongside `blind-trust`, `hallucination-in-prod`, `vibe-coding`, etc.
- Do NOT use for non-AI automation failures (use `automation` cause instead)
- Do NOT mix with infrastructure failures unless AI was the root cause

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
- `documentation-heavy` — relying on docs instead of intuitive design
- `short-term-incentives` — bonuses tied to quarterly results over long-term health
- `fear-of-cannibalization` — protecting legacy products at expense of innovation
- `innovators-dilemma` — inability to disrupt oneself
- `decision-making-by-proxy` — relying on AI/tools to make strategic calls

---

## Detailed Failure Patterns (Granular)

### AI & Automation Specifics
- `agent-failure` — specific failure of an autonomous agent
- `agent-loops` — infinite recursive loops
- `agentic-migration` — AI managing DB/infra migration
- `agentic-workflow` — multi-step AI processes
- `ai-assistant` — co-pilots and coding assistants
- `ai-generated-code` — specific code generation failures
- `ai-generated-codebase` — entire projects written by AI
- `ai-summaries` — risk of summarization loss
- `autonomous-ops` — AI managing infrastructure
- `chatbot-failure` — conversational interfaces failing
- `content-strategy` — AI content farms
- `coordination-failure` — multi-agent systems failing to sync
- `cost-explosion` / `cost-runaway` — unintended financial drain
- `hallucination` — factual fabrication
- `low-quality-content` — SEO spam or degradation
- `model-collapse` — retraining on synthetic data
- `multi-agent` / `multi-agent-llm` — swarm failures
- `rag-degradation` — retrieval quality issues
- `recursive-delegation` — agents calling agents indefinitely
- `runaway-agents` — loss of control over agent execution
- `schema-hallucination` — AI inventing database structures
- `synthetic-recursion` — data poisoning loop
- `token-bloat` / `token-explosion` — inefficient context usage
- `verification-gap` — inability to check AI outputs
- `vibe-coding` — coding by feel without understanding
- `video-generation` — video specific AI failures

### Security Specifics
- `account-takeover` — user account compromise
- `adversarial` / `adversarial-input` — malicious inputs
- `authentication-bypass` — skipping login checks
- `backdoor-insertion` — malicious code layout
- `bec` — business email compromise
- `build-infrastructure-compromise` — CI/CD attacks
- `cloud-misconfiguration` — publicly exposed resources
- `code-exfiltration` — source code theft
- `config-injection` — attacks via configuration files
- `credential-compromise` / `credential-lateral-movement` — identity theft
- `data-corruption` — integrity loss
- `data-exfiltration` — stealing data
- `feature-file-poisoning` — config files causing denial of service
- `iam` — identity and access management failures
- `mfa-fatigue` — spamming requests to bypass human check
- `nation-state-access` — APT involvement
- `oauth-misconfiguration` — flawed auth logic implementation
- `oauth-parameter-injection` — specifc attack vector
- `over-privileged-access` — violating least privilege
- `pii-exfiltration` — personal data theft
- `prompt-injection` — attacking LLMs via text
- `redirect-uri` — open redirect vulnerabilities
- `regulatory-fine` — financial penalty from government
- `secrets-exposure` — api keys/tokens leaked
- `social-engineering` — hacking humans
- `source-code-leak` — repo exposure
- `ssrf` — server side request forgery
- `supply-chain` — multiple variants
- `token-leakage` / `token-exposure` — specific OAuth/API token leaks
- `unpatched` — known vulnerabilities left open
- `zero-day` — unknown vulnerabilities exploited

### Infrastructure & Outage Specifics
- `backtracking` — regex performance issue
- `backup-failure` — restores failing
- `blast-radius` — impact area controls
- `business-logic-bypass` — flaw in app logic
- `capacity` — scaling limits
- `cascade` / `cascading-failure` — ripple effects
- `config-propagation` — how bad configs spread
- `cpu-exhaustion` — resource starvation
- `ddos-rule` — specific mitigation failures
- `dead-code` — unused code causing issues
- `deployment-failure` / `deployment-validation` — rollout issues
- `edge-computing` — CDN/Edge specific failures
- `error-spike` — monitoring signal
- `global-impact` / `global-outage` — worldwide downtime
- `hidden-sop` — secret operating procedures
- `kill-switch` — missing emergency stop
- `latent-bug` — dormant issue triggered later
- `no-escalation` — support failures
- `no-limits` — lacking rate limits/quotas
- `no-review` — skipping code review
- `no-rollback` — inability to revert
- `no-segmentation` — flat network/architecture
- `performance-loss` — degradation
- `premature` — launching too early
- `rec-fail` — recovery failure
- `region-dependency` / `regional-outage` — availability zone failures
- `replication` — database sync issues
- `rollback-failure` — specific failure of revert mechanism
- `system-design` — fundamental architecture flaws
- `systemic-outage` — total system collapse
- `trading-automation` — algorithmic trading failures
- `typo` — human input errors
- `visibility-loss` — monitoring blindness

### Product & Market Specifics
- `app-gap` — missing ecosystem apps
- `enterprise-pivot` — changing strategy to B2B
- `fashion` — wearable tech issues
- `late-entry` — missing market window
- `missed-opportunity` — strategy failure
- `premium-content` — business model failure
- `privacy` — user privacy concerns as product risk
- `user-acceptance` — social rejection of tech
- `wrong-assumptions` — incorrect axioms
- `wrong-market` — targeting wrong user base

### Additional Patterns (Granular)
- `automation-bias`
- `automation-without-review`
- `autonomous-systems`
- `brand-damage`
- `budget-explosion`
- `cloud-security`
- `collaboration-complexity`
- `customer-support`
- `data-degradation`
- `decision-degradation`
- `detection-failure`
- `ecosystem-failure`
- `endpoint-security`
- `github-access`
- `privileged-access`
- `production-bug`
- `rce-global`
- `regex`
- `s3-public-access`
- `seo-collapse`
- `shared-dependency`
- `social-media`
- `solarwinds`
- `trust-destruction`
- `trust-exploitation`
- `twitter`
- `unmaintainable`
- `unsafe-feature`
- `write-access`
- `A2A` — Agent-to-Agent communication failures
- `blind-trust-in-ai` — trusting AI without verification (variation of blind-trust)



---

## Technology & Timeline Tags

### Technologies
- `apache-struts`
- `aws`
- `cloudflare` / `fastly`
- `copilot`
- `github-actions`
- `log4j`
- `mcp` (Model Context Protocol)
- `mysql` / `postgresql`
- `s3`
- `vcl` (Varnish Config Language)
- `waf` (Web Application Firewall)

### Timeline / Events
- `2020-major`
- `2021-critical` / `2021-major`
- `2023-pattern`
- `2024-major` / `2024-worst`
- `2025-active` / `2025-critical` / `2025-trend`

---

## Tagging Guidelines

1.  **At minimum**: every entry needs type, cause, stage, impact
2.  **Free tags**: add 2-5 relevant tags from above or create new ones
3.  **Be consistent**: if a pattern appears in multiple entries, use the same tag
4.  **AI agents**: tags enable RAG retrieval and pattern matching
5.  **Searchability**: well-tagged entries help both humans and AI find relevant failures
