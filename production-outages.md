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

### (2018) GitHub — MySQL Replication Failure

```yaml
---
type: outage
cause: architecture
stage: scale
impact: users
tags: [hidden-dependency, rollback-failure, observability-gap, mysql, replication]
---

**What happened:** A routine maintenance operation triggered a large-scale MySQL replication failure, causing hours of downtime across GitHub's platform.

**Impact:** GitHub unavailable globally; deploys blocked; CI/CD pipelines halted; significant developer productivity loss.

**Root cause:** Overconfidence in replication infrastructure; insufficient understanding of failure modes; restore paths never tested; assumed backups were sufficient without validation.

**Lessons:**
- Backups are useless if restore paths aren't tested
- "We've done this before" is not a safety guarantee
- Understand failure modes before they happen
- Operational confidence ≠ operational safety

**Source:** https://github.blog/2018-10-30-october-incident-report/
```

### (2017) AWS — S3 Typo Takes Down us-east-1

```yaml
---
type: outage
cause: human-error
stage: scale
impact: users
tags: [blast-radius, control-plane, region-dependency, s3, typo]
---

**What happened:** A typo during debugging commands took down S3 in the us-east-1 region, cascading into major internet outages for thousands of services.

**Impact:** Thousands of services offline; major websites inaccessible; AWS dashboard unavailable; extended recovery time due to cascading effects.

**Root cause:** Human error during debugging; insufficient blast-radius controls; region-level dependencies as silent killers; recovery process itself caused delays.

**Lessons:**
- "Highly available" doesn't mean invulnerable
- Region-level dependencies are silent killers
- Debugging in production requires extreme caution
- Recovery procedures must be tested and resilient

**Source:** https://aws.amazon.com/message/41926/
```

### (2012) Knight Capital — $440M Trading Loss in Minutes

```yaml
---
type: outage
cause: automation
stage: scale
impact: money
tags: [no-rollback, deployment-failure, trading-automation, dead-code, kill-switch]
---

**What happened:** A faulty deployment activated dead code paths in Knight Capital's trading system, triggering uncontrolled trading that lost approximately $440M in under an hour.

**Impact:** Firm effectively destroyed; bankruptcy followed; market disruption; regulatory scrutiny.

**Root cause:** Broken deployment process; dead code left in production; no kill switches; automation without human oversight; deployment occurred during market hours.

**Lessons:**
- Automation without kill switches is lethal
- Old code is still production code — audit and remove dead paths
- Deployments during critical operations require extreme caution
- Every automated system needs a tested emergency stop

**Source:** https://www.sec.gov/spotlight/equity-markets-structure-committee/knight-capital-report.pdf
```

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
