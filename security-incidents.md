# Security Incidents 🔐

Breaches, data exposures, misconfigurations, and the trust failures they create.

---

## Entry Template

```yaml
---
type: security
cause: [human-error|architecture|incentives|automation]
stage: [early|growth|scale|decline]
impact: [data-loss|trust|money|users]
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

## Data Breaches

### (2017) Equifax — Unpatched Vulnerability

```yaml
---
type: security
cause: human-error
stage: scale
impact: data-loss
tags: [unpatched, apache-struts, credential-lateral-movement, no-segmentation, regulatory-fine]
---

**What happened:** Attackers exploited a known Apache Struts vulnerability (CVE-2017-5638) that had a patch available for 2 months. The breach exposed 147.9 million Americans' data including SSNs, birth dates, and addresses.

**Impact:** 147.9 million people affected; $1.38 billion in total costs including settlements and fines; massive reputational damage; executive departures.

**Root cause:** Failure to patch a critical vulnerability despite knowing about it. No network segmentation allowed lateral movement. Plaintext credentials enabled broader access. Existed for 76 days before detection.

**Lessons:**
- Patch critical vulnerabilities within hours/days, not weeks/months
- Network segmentation limits blast radius of initial compromise
- Store credentials securely; plaintext access enables lateral movement
- Detection time matters as much as prevention

**Source:** https://www.breachsense.com/blog/equifax-data-breach/
```

---

## Misconfigurations

## Supply Chain Attacks

## Authentication Failures

## Human Factor & Social Engineering
