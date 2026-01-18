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

### (2019) Capital One — Cloud Firewall Misconfiguration

```yaml
---
type: security
cause: human-error
stage: scale
impact: trust
tags: [misconfiguration, iam, ssrf, cloud-security, over-privileged-access]
---

**What happened:** An attacker exploited a misconfigured cloud firewall combined with a server-side request forgery (SSRF) vulnerability to access sensitive customer data stored in AWS.

**Impact:** Approximately 100 million customer records exposed; names, addresses, credit scores, and bank account numbers compromised; $80M regulatory fine; significant reputational damage.

**Root cause:** Misconfigured IAM roles with over-privileged access; internal services assumed trusted without validation; firewall rules too permissive; SSRF vulnerability in web application firewall.

**Lessons:**
- Cloud security failures are often configuration, not complex exploits
- Assume internal services will be abused — apply zero-trust principles
- IAM permissions should follow least-privilege, always
- Regular configuration audits catch what vulnerability scans miss

**Source:** https://www.justice.gov/opa/press-release/file/1244101/download

**Related failure patterns:**
- Misconfigured Trust Boundaries

```

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

**Related failure patterns:**
- Patching Debt

```

---

## Misconfigurations

## Supply Chain Attacks

## Authentication Failures

## Human Factor & Social Engineering
