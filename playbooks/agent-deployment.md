# Prevention Playbook: AI Agent Deployment 🛡️

Use this playbook when moving an AI agent from prototype to production. This expands on the [AI Agent Pre-Flight Checklist](../ai-agent-checklist.md) with specific technical implementation steps.

---

## 🟢 Phase 1: Environment Isolation (The Sandbox)

### 1. Minimal Access Tokens
Never use a master API key. Generate an IAM role or scoped API token that only has access to:
- Specific S3 buckets (not all)
- Specific database tables (via a service-user)
- Read-only access by default

### 2. Mocking Destructive Tools
If the agent can execute code or database queries:
- **Test:** Use a mock tool that returns the *plan* instead of executing.
- **Prod:** Wrap the tool in a "safe-executor" that validates the SQL or command against a blocklist (e.g., no `DROP`, `TRUNCATE`, `rm -rf /`).

---

## 🟡 Phase 2: Budgeting & Circuit Breakers

### 1. Hard Token Limits
Configure your LLM client (LangChain, OpenAI, etc.) with a `max_tokens` limit per request AND a `total_tokens` counter for the current session.

### 2. The $10 Kill-Switch
Implement a middleware that checks the real-time cost of the session.
```python
if session.accumulated_cost > 10.00:
    session.terminate(reason="Budget exceeded")
    alert_oncall("Agent stopped due to budget limit")
```

---

## 🔴 Phase 3: Human-in-the-Loop (HITL)

### 1. The "Approval Buffer"
For any action tagged as `destructive: true`, the agent must push the proposed action to a queue (e.g., Redis or Slack) and wait for a signed approval token before executing.

### 2. Explanation of Reasoning
Require the agent to output the "Reasoning Process" (Chain of Thought) before every tool call. If the reasoning doesn't match the action, the HITL reviewer should reject it.

---

## 🔵 Phase 4: Observability

### 1. Structured Logging
Log every agent thought, tool call, and tool output in NDJSON format for easy post-incident analysis.

### 2. Semantic Monitoring
Monitor agent outputs for "confidence markers." If an agent uses phrases like "I am unsure" or "I think this might work," trigger an automatic escalation to a human operator.
