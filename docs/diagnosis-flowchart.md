# Failure Diagnosis Flowchart 🩺

Use this flowchart to quickly categorize and identify recurring patterns when an incident occurs.

---

## High-Level Diagnosis

```mermaid
flowchart TD
    A[Incident Detected] --> B{AI Involved?}
    
    B -- Yes --> C{Agent or Content?}
    C -- Agent --> D{Runaway Costs?}
    D -- Yes --> E[Pattern: Automation Without Reversal]
    D -- No --> F{Destructive Action?}
    F -- Yes --> G[Pattern: Blind Trust / No Guardrails]
    F -- No --> H[Pattern: Misconfigured Trust Boundaries]
    
    C -- Content --> I{Shipped to Prod?}
    I -- Yes --> J[Pattern: AI Slop / Blind Trust]
    I -- No --> K[Pattern: Vibe Coding]
    
    B -- No --> L{Infra Failure?}
    L -- Yes --> M{Global Impact?}
    M -- Yes --> N[Pattern: Hidden SOP / Control Plane]
    M -- No --> O[Pattern: Human Error / Typos]
    
    L -- No --> P{Security Breach?}
    P -- Yes --> Q{Internal Access?}
    Q -- Yes --> R[Pattern: Misconfigured Trust Boundaries]
    Q -- No --> S[Pattern: Patching Debt]
```

---

## Pattern-Specific Checklists

### 🤖 AI Agent Failures
- [ ] Was there a hard token/cost limit?
- [ ] Did the agent have write access without human-in-the-loop?
- [ ] Can the action be reversed (rollback/undo)?

### 🏗️ Infrastructure Outages
- [ ] Is there a hidden shared dependency?
- [ ] Was the safety mechanism disabled or bypassed?
- [ ] Is the recovery path (backups/DR) tested?

### 🔐 Security Incidents
- [ ] Is this a known vulnerability with an available patch?
- [ ] Was an internal service assumed to be "trusted"?
- [ ] Could network segmentation have limited the blast radius?
