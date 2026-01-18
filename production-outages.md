# Production Outages 💥

Infrastructure failures, availability incidents, cascading system breakdowns,
and the postmortems that made them useful.

---

## Entry Template

```yaml
---
type: outage
cause: [automation|architecture|human-error|incentives]
stage: [early|growth|scale|decline]
impact: [data-loss|money|trust|users]
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

## Core Infrastructure Failures

### (2019) Cloudflare — Regex Catastrophe

```yaml
---
type: outage
cause: architecture
stage: scale
impact: trust
tags: [regex, backtracking, cpu-exhaustion, waf, global-impact, cascade]
---

**What happened:** A single regex rule deployed to Cloudflare's WAF caused CPU exhaustion across all HTTP/HTTPS servers worldwide, resulting in 30+ minutes of 502 errors for sites using Cloudflare.

**Impact:** Millions of websites unreachable; major services (Discord, Okta, others) affected; significant trust damage for a core internet infrastructure provider.

**Root cause:** The regex `.*(?:.*=.*)` caused catastrophic backtracking. The rule wasn't tested for CPU impact. A safety mechanism that would have limited CPU usage had been removed weeks earlier "by mistake."

**Lessons:**
- Test regex performance before deployment, especially in WAF rules
- Any change to safety mechanisms requires review and rollback plan
- Monitor CPU usage in test suites, not just functionality
- Single points of failure in safety systems are catastrophic

**Source:** https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/
```

---

## Data Loss & Corruption

## Cascading Failures

## Observability Failures

## Rollback Failures
