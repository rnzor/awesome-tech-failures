# Awesome Tech Failures 💥

Failure is data.

A curated, tagged library of real-world tech failures — outages, breaches, startup shutdowns, product flops, **AI slop**, and automation disasters.

**Goal:** learn faster by studying what broke, why it broke, and what actually fixed it.

> Success stories sell. Failure stories teach.

---

## Why this repo exists

The tech industry is full of success stories.

They are polished.
They are incomplete.
They often lie by omission.

This repo exists for the other half of reality.

---

### Failure is data

Outages, breaches, failed startups, bad products, and broken AI systems
are not embarrassing footnotes — they are **primary learning material**.

Modern systems fail in modern ways:
- automation without rollback
- AI used without understanding
- speed optimized over responsibility
- decisions made by proxy instead of judgment

We document those failures so they don't have to be rediscovered the hard way.

---

### What this repo is

- A **curated library** of real-world tech failures
- A **pattern map**, not just a link dump
- A place where **AI slop and automation failures are treated seriously**
- A resource for **engineers, founders, operators — and AI agents**

Every entry focuses on:
- what happened
- why it happened
- what actually mattered in fixing (or failing to fix) it

---

### What this repo is not

- Not a hype repository
- Not "AI will save us" content
- Not blame-driven or sensational
- Not fictional or speculative

If something is a repeated pattern rather than a single incident, we label it honestly.

---

### Why this matters now

We ship faster than ever.
We automate decisions.
We delegate thinking to tools.

But responsibility doesn't disappear — it just moves.

AI doesn't remove failure.
It changes *how* failure happens.

This repo helps you recognize those patterns **before** they show up in your own systems.

---

### How to use this repo

- **Humans:**  
  Before shipping automation, agents, rewrites, or strategy shifts — scan the patterns.

- **AI agents:**  
  Use failure patterns as negative priors:  
  "This plan resembles known failures with these tags."

---

### One rule of thumb

> AI should remove **toil**, not **responsibility**.

If responsibility moved to the model, you already lost.

---

## How this repo works

Each entry has:
- **What happened** (1–2 lines)
- **Impact** (who/what got hit)
- **Root cause** (best-known)
- **Lessons** (actionable)
- **Tags** (so humans & AI agents can search patterns)

If you ship AI agents or automation: start with **AI Slop & Automation**.

---

## Sections

- [AI Slop & Automation Failures](ai-slop-and-automation.md)
- [Production Outages](production-outages.md)
- [Security Incidents](security-incidents.md)
- [Startup Failures](startup-failures.md)
- [Product & Strategy Failures](product-failures.md)
- [Decision & Process Failures](decision-failures.md)
- [Failure Patterns Index](failure-patterns.md)
- [Tags Reference](tags.md)

---

## Entry format (TL;DR)

```yaml
type: ai-slop | outage | security | startup | product | decision
cause: human-error | automation | incentives | architecture | ai
stage: early | growth | scale | decline
impact: data-loss | money | trust | users | morale
tags: [prompt-injection, runaway-costs, blind-trust, rollback-failure]
```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

High signal only. Primary sources preferred. No "failure porn".
