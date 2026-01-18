<!--
ai-agent-checklist.md: Human-readable pre-flight guide for deploying AI agents.
For machine-readable agent policies, see AGENTS.md and agent/policies/
-->

---
type: guide
tags: [ai-agent, automation, safety, checklist, pre-flight]
related-patterns:
  - Automation Without Reversal
  - Blind Trust in AI Output
  - Misconfigured Trust Boundaries
  - Decision-Making by Proxy
---

# AI Agent Pre-Flight Checklist

Use this before deploying AI agents, automation, or AI-assisted workflows in production.

This checklist exists because most AI failures are not model failures —
they're design, permission, and responsibility failures.

---

## 0. Hard Rule (Read This First)

If an AI agent can cause damage, it must be easier to stop than to start.

If that's not true, stop here.

---

## 1. Scope & Authority

**Questions**

- What exactly is this agent allowed to do?
- What is explicitly forbidden?
- Can it affect production data, money, users, or trust?

**Red flags**

- "It just does what's needed"
- "We'll see what it does in prod"
- "It probably won't touch that"

**Required**

- Narrow, explicit scope
- Separate read vs write permissions
- Environment isolation (dev ≠ prod)

**Related patterns**
- Automation Without Reversal
- Misconfigured Trust Boundaries

---

## 2. Write Access & Irreversibility

**Questions**

- Can the agent delete, modify, or publish anything?
- Are all write actions reversible?
- Is rollback cheaper than execution?

**Red flags**

- No undo path
- Deletes instead of soft-deletes
- "We'll restore from backup"

**Required**

- Dry-run mode
- Soft deletes / versioning
- Rollback tested, not assumed

**Related patterns**
- Automation Without Reversal

---

## 3. Human-in-the-Loop Boundaries

**Questions**

- Which decisions must require human approval?
- Where does the agent stop and escalate?

**Red flags**

- "The agent decides"
- No escalation path
- Humans only notice after damage

**Required**

- Explicit approval gates
- Clear ownership ("who stops it?")
- Fast manual override

**Related patterns**
- Blind Trust in AI Output
- Decision-Making by Proxy

---

## 4. Input Trust & Prompt Safety

**Questions**

- Can users influence prompts or tool inputs?
- Are prompts treated as untrusted input?

**Red flags**

- User input merged directly into system prompts
- Tools exposed without validation
- "It's just text"

**Required**

- Input sanitization
- Prompt boundary separation
- Tool call allowlists

**Related patterns**
- Misconfigured Trust Boundaries

---

## 5. Observability & Explainability

**Questions**

- Can you tell why the agent did something?
- Can you replay or audit decisions?

**Red flags**

- "The model decided"
- No logs for reasoning or tool calls
- No timeline of actions

**Required**

- Structured logs
- Action traces
- Decision context retention

**Related patterns**
- Overconfidence From Past Success

---

## 6. Cost & Resource Controls

**Questions**

- What is the maximum cost per hour/day?
- What happens if the agent loops?

**Red flags**

- No token limits
- No execution budget
- "We'll notice on the bill"

**Required**

- Hard budgets
- Rate limits
- Loop detection / execution caps

**Related patterns**
- Automation Without Reversal

---

## 7. Failure Modes (Assume It Will Be Wrong)

**Questions**

- How does the system fail safely?
- What happens when the model hallucinates?

**Red flags**

- Assuming correctness
- No fallback behavior
- Silent failures

**Required**

- Explicit failure paths
- Safe defaults
- Clear error surfacing

**Related patterns**
- Blind Trust in AI Output

---

## 8. Ownership & Responsibility

**Questions**

- Who is accountable if this breaks?
- Who gets paged at 3am?

**Red flags**

- "The AI did it"
- Shared responsibility
- No on-call owner

**Required**

- Single owner
- Clear escalation chain
- Runbook for agent failure

**Related patterns**
- Decision-Making by Proxy

---

## 9. Can You Turn It Off?

**Final test**

- Can you disable the agent immediately?
- Without redeploying?
- Without asking the agent itself?

If the answer is "no" → do not ship.

---

## One-Line Sanity Check

> If this agent were a junior employee with prod access, would you still let it run unattended?
>
> If not, fix the design.

---

## How to Use This Checklist

- Paste it into PRs introducing AI agents
- Run it during architecture reviews
- Convert it into automated policy checks
- Feed it to AI agents as a constraint, not advice

---

## Why This Exists

AI doesn't remove responsibility.
It concentrates it.

This checklist is here to stop you from learning that lesson the hard way.
