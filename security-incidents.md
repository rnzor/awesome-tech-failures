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

### (2021) Twitch — Source Code Leak via S3 Misconfiguration

```yaml
---
type: security
cause: human-error
stage: scale
impact: trust
severity:
  level: high
  score: 9
  financial: Significant
tags: [cloud-misconfiguration, s3-public-access, source-code-leak, secrets-exposure, 2021-major]
---

**What happened:** A server configuration change exposed internal Twitch infrastructure. An attacker downloaded 125GB of data, including Twitch's complete source code, internal tools, and creator payouts.

**Impact:** Complete source code for Twitch and subsidiaries exposed; 6,600+ secrets (AWS/GitHub keys) leaked. Massive intellectual property theft.

**Root cause:** Server configuration error during a system change made an S3 bucket or similar storage service publicly accessible.

**Lessons:**
- Configuration changes are the leading cause of cloud data exposure
- Secrets embedded in source code are a systemic vulnerability, not an edge case
- Once code is leaked, assume all embedded secrets are compromised; rotate aggressively

**Source:** https://www.bbc.com/news/technology-58817658

**Related failure patterns:**
- Blind Trust in AI Output
- Misconfigured Trust Boundaries
```

## Supply Chain Attacks

### (2020) SolarWinds — Orion Supply Chain Attack

```yaml
---
type: security
cause: architecture
stage: scale
impact: trust
severity:
  level: critical
  score: 10
  financial: Massive
tags: [supply-chain, build-infrastructure-compromise, nation-state-access, solarwinds, 2020-major]
---

**What happened:** APT29 (nation-state actor) compromised SolarWinds' software build process via SUNSPOT, injecting a backdoor (SUNBURST) into signed updates distributed to 30,000+ organizations.

**Impact:** US government agencies breached; nation-state actors gained persistent access to critical infrastructure; confirmed large-scale data theft.

**Root cause:** Attackers compromised the automated build process—a less obvious attack surface than source control. Malware masqueraded as legitimate traffic to hide exfiltration.

**Lessons:**
- Build infrastructure is as critical as source control; both require equal protection
- Supply chain attacks succeed by exploiting trust in software updates
- Cryptographic signing alone does not ensure integrity if the signing key is compromised

**Source:** https://cloud.google.com/blog/topics/threat-intelligence/sunburst-backdoor-analysis

**Related failure patterns:**
- Hidden Single Point of Failure
- Misconfigured Trust Boundaries
```

### (2025) GitHub — CodeQL Supply Chain Vulnerability

```yaml
---
type: security
cause: architecture
stage: scale
impact: trust
severity:
  level: critical
  score: 9
  financial: Massive Potential
tags: [supply-chain, token-exposure, code-exfiltration, github-actions, 2025-active]
---

**What happened:** A GitHub token was exposed in CodeQL Actions workflow artifacts for ~1 second, allowing attackers to capture it and modify immutable tags to point to malicious code.

**Impact:** Potential exfiltration of private source code from hundreds of thousands of repositories; compromise of high-profile targets like Angular and Grafana.

**Root cause:** Non-immutable tags in official actions; token exposure in workflow artifacts; failure to use workflow pinning.

**Lessons:**
- Supply chain attacks on CI/CD are effective; even brief token exposures are dangerous
- Immutable tags and workflow pinning are not optional for critical actions
- Cache poisoning is a persistent threat; cache hygiene is essential

**Source:** https://www.praetorian.com/blog/codeqleaked-public-secrets-exposure/

**Related failure patterns:**
- Misconfigured Trust Boundaries
- Hidden Single Point of Failure
```

## Zero-Day & Infrastructure Vulnerabilities

### (2021) Log4Shell — Global Remote Code Execution (CVE-2021-44228)

```yaml
---
type: security
cause: architecture
stage: scale
impact: trust
severity:
  level: critical
  score: 10
  financial: Massive
tags: [zero-day, unsafe-feature, rce-global, log4j, 2021-critical]
---

**What happened:** A remote code execution vulnerability in Apache Log4j 2 allowed attackers to execute arbitrary code by crafting log messages that triggered malicious JNDI lookups.

**Impact:** 93% of enterprise cloud environments affected; hundreds of millions of devices vulnerable. Exploited by major botnets and across multiple tech giants (AWS, Cloudflare).

**Root cause:** Log4j's message lookup feature did not validate or sandbox JNDI references. The flaw existed unnoticed in a core library since 2013.

**Lessons:**
- Dynamic code execution features (JNDI, deserialization) are inherently dangerous
- User-controlled input flowing to logging systems is a critical attack surface
- Widespread usage increases blast radius; patching at scale takes weeks/months

**Source:** https://logging.apache.org/log4j/2.x/security.html

**Related failure patterns:**
- Hidden Single Point of Failure
```

## Authentication Failures

### (2023–2025) Booking.com — OAuth Redirect URI Misconfiguration

```yaml
---
type: security
cause: human-error
stage: scale
impact: trust
severity:
  level: high
  score: 8
  financial: Significant
tags: [authentication-bypass, oauth-misconfiguration, account-takeover, redirect-uri, 2023-pattern]
---

**What happened:** Booking.com's OAuth implementation allowed open redirect vulnerabilities via loose path matching on the `redirect_uri` parameter.

**Impact:** Potential user account takeover on Booking.com and Kayak; authorization code and access token theft.

**Root cause:** Application-layer implementation did not enforce exact path matching for redirect URIs, despite domain-level validation.

**Lessons:**
- OAuth provider validation alone is insufficient; client applications must validate strictly
- Exact path matching is required; domain-only validation is too permissive
- Open redirects are especially dangerous in OAuth flows

**Source:** https://www.descope.com/blog/post/oauth-vulnerabilities

**Related failure patterns:**
- Misconfigured Trust Boundaries
```

### (2023–2025) Expo — OAuth Token Exposure via Return URL

```yaml
---
type: security
cause: architecture
stage: scale
impact: trust
severity:
  level: high
  score: 8
  financial: Significant
tags: [authentication-bypass, oauth-parameter-injection, account-takeover, token-leakage, 2023-pattern]
---

**What happened:** Expo's OAuth implementation allowed manipulation of the `returnURL` parameter to send OAuth tokens to attacker-controlled domains.

**Impact:** Mass user account takeover potential across any app using Expo's OAuth service.

**Root cause:** Insufficient validation of the `returnURL` parameter; trust in user-supplied redirect targets without verification.

**Evidence type:** Direct incident
Researcher-discovered OAuth vulnerability with documented exploitation path; specific incident with identified attack vector and named service.

**Lessons:**
- Return URL validation must be as strict as redirect URI validation
- OAuth proxies introduce additional validation requirements

**Source:** https://www.descope.com/blog/post/oauth-vulnerabilities

**Related failure patterns:**
- Misconfigured Trust Boundaries
```

## Human Factor & Social Engineering

### (2022) Uber — MFA Fatigue & Social Engineering

```yaml
---
type: security
cause: human-error
stage: scale
impact: trust
severity:
  level: high
  score: 9
  financial: Significant
tags: [social-engineering, mfa-fatigue, privileged-access, human-factor, data-exposure]
---

**What happened:** An attacker gained access to an Uber employee's account by bombarding them with MFA push notifications ("MFA fatigue") and then posing as IT help desk.

**Impact:** Attacker accessed internal Slack, G-Suite, and financial tools; exposed internal AWS and security dashboards.

**Root cause:** Reliance on simple push-based MFA; lack of internal zero-trust; human vulnerability to social engineering.

**Lessons:**
- Shift from push-based MFA to security keys to prevent fatigue attacks
- Apply zero-trust internally: password should not grant full access
- Regularly train employees on social engineering tactics

**Source:** https://www.uber.com/newsroom/security-update/

**Related failure patterns:**
- Misconfigured Trust Boundaries
- Overconfidence From Past Success
```

### (2025) Unit 42 — Social Engineering Trend Report

```yaml
---
type: security
cause: human-error
stage: scale
impact: trust
severity:
  level: high
  score: 8
  financial: Global Trend
tags: [human-factor, trust-exploitation, data-exfiltration, bec, 2025-trend]
---

**What happened:** Social engineering became the #1 initial access vector in 2025 (36% of incidents). 66% targeted privileged accounts.

**Impact:** Widespread credential theft, data exfiltration, and business email compromise (BEC).

**Root cause:** Attackers exploit human trust and urgency; weak access controls and over-permissioned accounts amplify initial compromises.

**Lessons:**
- Social engineering succeeds due to human behavior, not technical sophistication
- Weak controls (missing MFA, over-permissions) amplify social engineering impact
- Detection gaps and alert fatigue mask critical signals

**Source:** https://unit42.paloaltonetworks.com/global-incident-response-report/

**Related failure patterns:**
- Misconfigured Trust Boundaries
- Decision-Making by Proxy
```

### (2024) LexisNexis — GitHub Account Compromise via Social Engineering

```yaml
---
type: security
cause: human-error
stage: scale
impact: trust
severity:
  level: high
  score: 9
  financial: Significant
tags: [social-engineering, credential-compromise, pii-exfiltration, github-access, 2024-major]
---

**What happened:** An attacker gained access to LexisNexis's GitHub account via social engineering (pretext calls) and exfiltrated personal data for 364,000+ individuals.

**Impact:** Mass PII exposure including SSNs and driver's licenses.

**Root cause:** Weak authentication controls on GitHub and human vulnerability to pretexting.

**Lessons:**
- GitHub access is equivalent to internal infrastructure access
- Social engineering targets help desk and support; specific training is required
- Third-party development platforms often hold sensitive data; access must be strict

**Source:** https://techcrunch.com/2025/05/27/data-broker-lexisnexis-breach-exposed-364k-people/

**Related failure patterns:**
- Misconfigured Trust Boundaries
- Overconfidence From Past Success
```
