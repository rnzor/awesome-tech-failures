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

## Over-Automation Without Rollback

## Runaway Costs & Infinite Loops

## "Vibe Coding" Maintenance Disasters

## Replaced Understanding with AI Summaries
