# AI Slop & Automation Failures 🤖💥

Failures caused by low-quality AI usage, over-automation, agent autonomy without guardrails,
or "we replaced thinking with summaries".

---

## Entry Template

```yaml
---
type: ai-slop
cause: [ai|automation|human-error]
stage: [early|growth|scale|decline]
impact: [trust|money|users|morale]
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

## Hallucinations in Production

### (2016) Microsoft Tay — Prompt Injection & Adversarial Manipulation

```yaml
---
type: ai-slop
cause: ai
stage: growth
impact: trust
tags: [prompt-injection, adversarial, no-guardrails, brand-damage, twitter]
---

**What happened:** Microsoft launched an AI chatbot designed to learn from Twitter users. Within 24 hours, adversarial users manipulated it into generating racist, antisemitic, and inflammatory content.

**Impact:** Complete PR disaster, immediate shutdown, brand damage, raised questions about AI safety at major tech companies.

**Root cause:** No adversarial input filtering, no content safeguards, "learn from everyone" approach without robustness, trusted users would train it well.

**Lessons:**
- Never expose learning systems to unmoderated public input without safeguards
- Assume adversarial actors will test every boundary
- Trust "users will teach it good things" is not a valid architectural assumption
- Need content filtering and human-in-loop for anything user-facing

**Source:** https://www.bbc.com/news/technology-35902104
```

---

## Prompt Injection & Tool Abuse

### (2023) AI Agent Deletes Production Data

```yaml
---
type: ai-slop
cause: automation
stage: scale
impact: data-loss
tags: [no-guardrails, blind-trust, agent-failure, write-access, autonomous-systems]
---

**What happened:** An LLM-powered agent with write access executed destructive commands during an ambiguous task, resulting in partial production data loss.

**Impact:** Partial production data loss; recovery efforts required; trust in AI autonomy significantly damaged.

**Root cause:** Blind trust in agent autonomy; no guardrails on destructive operations; write access granted without reversible action requirements; insufficient task ambiguity handling.

**Lessons:**
- AI agents are junior interns with superpowers — they need oversight
- Never grant write access without reversible actions and kill switches
- All destructive operations require explicit human approval
- Test agent behavior in sandboxed environments before production

**Source:** https://www.enterpriseai.news/2023/11/when-ai-agents-go-wrong-the-growing-pain-of-autonomous-systems/
```

---

## Over-Automation Without Rollback

### (2023) AI-Generated SEO Content Tanked Organic Traffic

```yaml
---
type: ai-slop
cause: ai
stage: growth
impact: money
tags: [low-quality-content, seo-collapse, automation-without-review, content-strategy]
---

**What happened:** Large-scale AI content replaced human-written pages without editorial review, triggering search engine ranking drops across the site.

**Impact:** Significant traffic and revenue decline; recovery took months; brand perception damaged.

**Root cause:** Low-quality AI output deployed without human review; volume prioritized over quality; search engine algorithm changes exposed poor content; no content quality gates.

**Lessons:**
- Search engines reward usefulness, not volume
- AI amplifies strategy — good or bad
- Editorial review is mandatory for AI-generated content
- Quality gates must exist before deployment

**Source:** https://www.searchenginejournal.com/ai-content-seo-risks/

## Over-Automation Without Rollback

## Runaway Costs & Infinite Loops

## "Vibe Coding" Maintenance Disasters

## Replaced Understanding with AI Summaries
