# Incident Response Template 🚨

Copy this document when a major failure occurs. Fill it out in real-time.

**Incident Name:** [YYYY-MM-DD] <Short Descriptive Title>
**Severity:** [Critical | High | Medium | Low]
**Status:** [Investigating | Identified | Monitoring | Resolved]
**Commander:** @username

---

## 1. Immediate Actions (The "Stop the Bleeding" Phase)

- [ ] **Acknowledge:** Confirm incident in `#incidents` channel.
- [ ] **Assess:** Is this localized or global? (Check User Impact)
- [ ] **Contain:** Can we stop the harm?
  - [ ] Default to **Rollback** if a recent change was made.
  - [ ] Enable **Feature Flags** / Kill Switches.
  - [ ] Isolate the affected cell/shard.
- [ ] **Communicate:** Update status page (internal/external).

---

## 2. Context & Symptoms

| Metric | Status | Notes |
|:---|:---|:---|
| User Impact | 🔴 High | 50% of requests failing |
| Data Integrity | 🟡 Unknown | Checking backups |
| Revenue Impact | 🔴 High | Checkout flow broken |

**Timeline:**
- `00:00 UTC` - First alert fired (High Latency)
- `00:05 UTC` - On-call acknowledged
- `00:15 UTC` - Rollback initiated
- `...`

---

## 3. Investigation & Hypothesis

**Hypothesis A:** Database lock contention due to new migration.
- *Test:* Check `pg_stat_activity` for waiting queries.
- *Result:* [True/False]

**Hypothesis B:** AI Agent token limit exceeded.
- *Test:* Check LLM provider dashboard.
- *Result:* [True/False]

---

## 4. Resolution & Recovery

- **Action Taken:** [e.g., Reverted PR #1234]
- **Verification:** Services returning 200 OK. Error rates dropped to <1%.
- **Cleanup:** Restarted stuck pods. Clear caches.

---

## 5. Post-Incident Review (The Learning)

*To be filled out 24-48h after resolution.*

**Root Cause:**
[The "Why" behind the "What"]

**Trigger:**
[The specific event that started the cascade]

**Corrective Actions (P0/P1):**
1. [ ] Add circuit breaker to X service
2. [ ] Update runbook for Y scenario
3. [ ] Add test case for Z condition

**Related Patterns:**
- [Link to failure-patterns.md]
