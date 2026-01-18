# Prevention Playbook: Production Outage Guardrails 🏗️

Standard operating procedures (SOPs) based on lessons from AWS, GitHub, and Cloudflare outages.

---

## 🟢 1. Blast Radius Control

### Cell-Based Architecture
Partition your infrastructure so that a failure in one "cell" (region, cluster, or customer shard) cannot propagate to others.
- **Rule:** Global resources should only point to cells, never the other way around.

### Throttling & Integrity
Every internal API must have rate limits, even for sister services.
- **Lesson (Cloudflare):** Safety mechanisms should have dedicated, redundant resources that cannot be exhausted by the main traffic flow.

---

## 🟡 2. The Maintenance "Rule of Three"

Before running ANY maintenance command that touches production data:
1. **The Verification:** Run a "Dry Run" or `EXPLAIN` and peer-review the output.
2. **The Backup:** Verify that a restorable backup exists (don't just check the cron log).
3. **The Rollback:** Write the exact "undo" command before running the "do" command.

---

## 🔴 3. Automation Safeguards

### Human-in-the-Loop for Bulk Actions
Any automation that touches more than 10% of users or resources simultaneously must require a manual "Proceed" click.

### Canary Deployments
Automated deployments should always hit 1% of traffic first.
- **Success Metric:** No increase in 5xx errors or CPU latency over 10 minutes.
- **Auto-Rollback:** If metrics fail, the system should revert automatically without human intervention.

---

## 🔵 4. Testing the Absence

### Chaos Engineering
Regularly "unplug" core dependencies (DNS, Auth, Database) in a staging environment to see how the system fails.
- **Goal:** Graceful degradation. The system should still allow read-only access if the primary database is down.

### Game Days
Simulate a major outage (e.g., S3 us-east-1 being down) once a quarter to verify that the team knows the recovery path and has the correct permissions.
