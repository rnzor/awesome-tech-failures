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
impact: [users]
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

**Related failure patterns:**
- Hidden Single Point of Failure
- Overconfidence From Past Success

```

### (2017) AWS — S3 Typo Takes Down us-east-1

```yaml
---
type: outage
cause: human-error
stage: scale
impact: [users]
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

**Related failure patterns:**
- Hidden Single Point of Failure
- Automation Without Reversal

```

### (2012) Knight Capital — $440M Trading Loss in Minutes

```yaml
---
type: outage
cause: automation
stage: scale
impact: [money]
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

**Related failure patterns:**
- Automation Without Reversal

```

### (2019) Cloudflare — Regex Catastrophe

```yaml
---
type: outage
cause: architecture
stage: scale
impact: [trust]
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

**Related failure patterns:**
- Automation Without Reversal
- Overconfidence From Past Success

```

---

## Data Loss & Corruption

### (2017) GitLab — Sysadmin Deletes Database during Maintenance

```yaml
---
type: outage
cause: human-error
stage: scale
impact: [data-loss]
tags: [data-loss, backup-failure, human-error, postgresql, replication]
---

**What happened:** During a routine maintenance window to resolve replication lag, a tired system administrator accidentally deleted 300GB of live production data by running `rm -rf` on the wrong directory.

**Impact:** 18 hours of downtime for GitLab.com; loss of project metadata, comments, and bug reports; git repositories themselves were safe but database state was lost.

**Root cause:** Human error due to fatigue and lack of guardrails; five different levels of backups and replication failed or were found to be empty; backup verification process was non-existent.

**Lessons:**
- Backups are only as good as your last successful restore test
- Implement guardrails for destructive commands (e.g., alias `rm` to interactive mode)
- Monitor backup size and completion — don't assume success
- Engineer systems to be resilient to human error at 2 AM

**Source:** https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/

**Related failure patterns:**
- Automation Without Reversal
- Overconfidence From Past Success

```

## Cascading Failures

### (2021) Fastly — Single Customer Config Triggering Global Outage

```yaml
---
type: outage
cause: architecture
stage: scale
impact: [users]
tags: [vcl, global-outage, cascading-failure, edge-computing, hidden-sop]
---

**What happened:** A single valid configuration change by one customer triggered a software bug in Fastly's edge cloud, causing 85% of their network to return 503 errors within minutes.

**Impact:** Major websites like Reddit, Twitch, and NYT went dark globally for approximately an hour; significant traffic drop across the internet.

**Root cause:** A dormant bug in the VCL (Varnish Configuration Language) compiler was triggered by a specific set of configuration parameters; failure to isolate service-wide impacts from individual customer changes.

**Lessons:**
- Individual customer actions should never be able to trigger global infrastructure failures
- Implement "cell-based architecture" to limit blast radius
- Dormant bugs in critical path code are time bombs — fuzzing matters
- Fast rollbacks are the best defense against unknown-condition triggers

**Source:** https://www.fastly.com/blog/summary-of-june-8-incident

**Related failure patterns:**
- Hidden Single Point of Failure
- Automation Without Reversal

```

### (2025) Cloudflare — Bot Management Feature File Corruption

```yaml
---
type: outage
cause: automation
stage: scale
impact: [users]
severity:
  level: high
  score: 9
  financial: Significant
tags: [cascading-failure, config-propagation, global-outage, feature-file-poisoning, 2025-active]
---

**What happened:** A database permission change caused the Bot Management feature file to double in size. This oversized file exceeded the size limits of routing software deployed across Cloudflare's global network.

**Impact:** Thousands of sites unreachable including X, ChatGPT, Spotify, and Discord for 30-90 minutes. Millions of users affected globally.

**Root cause:** A change to database system permissions unexpectedly multiplied feature file entries. The software had a hard limit on file size that was not enforced upstream. No size-limit validation caught the problem before propagation.

**Lessons:**
- Configuration changes can have exponential downstream effects; test at scale before global rollout
- Size limits and capacity checks must be enforced at the source, not at consumption
- Distinguish DDoS attack signatures from internal cascading failures early

**Source:** https://blog.cloudflare.com/outage-report-november-18-2025/

**Related failure patterns:**
- Hidden Single Point of Failure
- Automation Without Reversal

```

### (2024) Meta — Shared Infrastructure Cascading Failure

```yaml
---
type: outage
cause: architecture
stage: scale
impact: [users]
severity:
  level: high
  score: 8
  financial: Significant
tags: [cascading-failure, shared-dependency, global-outage, social-media, 2024-major]
---

**What happened:** A technical issue in Meta's infrastructure caused cascading failures across Facebook, Instagram, Threads, WhatsApp, and Messenger.

**Impact:** Hundreds of millions of users unable to communicate; major business disruption for advertisers and creators. Peak complaints exceeded 170k globally.

**Root cause:** Infrastructure-level issue cascaded across multiple services due to shared backend dependencies.

**Lessons:**
- Shared infrastructure creates cascading risk; failures in one service ripple to others
- Complex interdependencies are invisible until they fail
- Long MTTR indicates poor incident detection or response coordination

**Source:** https://www.cnbc.com/2024/12/11/metas-facebook-instagram-go-down.html

**Related failure patterns:**
- Hidden Single Point of Failure
- Overconfidence From Past Success

```

## Observability Failures

### (2025) AWS — CloudWatch & Health Dashboard Co-Located Failure

```yaml
---
type: outage
cause: architecture
stage: scale
impact: [visibility-loss]
severity:
  level: high
  score: 8
  financial: Indirect
tags: [observability-gap, architecture, visibility-loss, regional-outage, 2025-critical]
---

**What happened:** An AWS outage in US-East-1 took down production workloads and simultaneously took down the observability stack (CloudWatch, Health Dashboard) hosted in the same region.

**Impact:** Engineers were blind and unable to diagnose the root cause in real time. Delayed root cause analysis and extended incident response time.

**Root cause:** Architectural decision to co-locate monitoring infrastructure with production workloads. Observability systems lacked geographic redundancy.

**Lessons:**
- Observability must be external to the systems being monitored
- Regional failures require monitoring in separate regions or managed third-party services
- AI and automation cannot help if you are blind during the incident

**Source:** https://www.linkedin.com/pulse/when-observability-fails-what-we-can-learn-from-aws-outage/

**Related failure patterns:**
- Hidden Single Point of Failure
- Decision-Making by Proxy

```

## Rollback Failures

### (2024) CrowdStrike — Faulty Falcon Sensor Update

```yaml
---
type: outage
cause: deployment-validation
stage: scale
impact: [systemic-outage]
severity:
  level: critical
  score: 10
  financial: $5B+
tags: [rollback-failure, cause:deployment-validation, systemic-outage, endpoint-security, 2024-worst]
---

**What happened:** CrowdStrike deployed a faulty update to its Falcon sensor, triggering system crashes on millions of Windows devices globally. Rollback required physical access to machines.

**Impact:** $5+ billion in direct losses; hospitals, airlines, and banks grounded globally. Largest IT outage in history.

**Root cause:** Insufficient pre-deployment testing or staged rollout. The update was deployed globally without canary validation. Rollback required human intervention at scale.

**Lessons:**
- Endpoint agent updates require the most rigorous testing; global blast radius is total
- Canary deployments are non-negotiable for critical infrastructure
- Rollbacks that require physical access are not rollbacks; they are disasters

**Source:** https://www.crowdstrike.com/blog/falcon-content-update-remediation-and-guidance-hub/

**Related failure patterns:**
- Automation Without Reversal
- Overconfidence From Past Success

```

### (2024) Cloudflare — DDoS Rule Deployment Failure

```yaml
---
type: outage
cause: latent-bug
stage: scale
impact: [error-spike]
severity:
  level: medium
  score: 7
  financial: Significant
tags: [rollback-failure, cause:latent-bug, error-spike, ddos-rule, 2024-major]
---

**What happened:** A new DDoS mitigation rule triggered a latent bug in the rate-limiting system, causing HTTP request handling processes to use excessive CPU globally.

**Impact:** Significant global error spike (1-3%) and 3x latency increase for hours. Engineers initially misdiagnosed as an external attack.

**Root cause:** New DDoS rule contained a broken cookie validation check that triggered an exception. Latent interaction was not exercised during pre-deployment testing.

**Lessons:**
- Latent bugs in stable code can be triggered by new code paths; interaction testing is essential
- Gradual global rollout is good practice, but must include staged failure detection
- Distinguish internal cascades from external attacks immediately

**Source:** https://blog.cloudflare.com/incident-report-june-20-2024/

**Related failure patterns:**
- Hidden Single Point of Failure
- Overconfidence From Past Success

```
