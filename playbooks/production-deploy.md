# Prevention Playbook: Production Deployment 🚀

**Target Audience:** Engineers deploying code or config changes.
**When to use:** Before merging to `main` or deploying to production.

---

## 1. The Pre-Merge Contract

- [ ] **Code Review:** Approved by at least one domain expert.
- [ ] **AI Code Verified:** If AI wrote the code, a human has explicitly verified it understands the logic (no "vibe coding").
- [ ] **Rollback Plan:** I know exactly how to undo this change in < 1 minute.
  - [ ] Revert PR
  - [ ] Toggle Feature Flag
  - [ ] Restore Database Snapshot
- [ ] **Database Migrations:**
  - [ ] Down-migration script tested locally.
  - [ ] `lock_timeout` set to prevent production halts.
  - [ ] Non-destructive changes only (expand-contract pattern).

---

## 2. The Deployment Window

- [ ] **Timing:** Is it Friday at 5 PM? Unless it's a P0 fix, **STOP**.
- [ ] **Staffing:** Is the on-call engineer available and aware?
- [ ] **Status:** Is the platform currently stable? (Check status page).

---

## 3. The Release (Canary / Staged)

1. **Deploy to Staging:** Verify happy path AND failure limits.
2. **Deploy to Canary (1%):**
   - Check logs for new `ERROR` or `WARN` lines.
   - Check latency (p95 and p99).
   - Check CPU/Memory profiles.
3. **Deploy to 10% -> 50% -> 100%:**
   - Wait 5-10 minutes between steps.
   - "Bake time" is the enemy of regressions.

---

## 4. Post-Deploy Verification

- [ ] **Observability:** Dashboards look nominal.
- [ ] **User Feedback:** Support tickets are normal.
- [ ] **Clean up:** Delete old feature flags if 100% rolled out.

---

> "Deployment is not success. Used, working, and valuable software is success."
