<!--
AGENTS.md: Operating policy for AI agents consuming this repo.
For human-readable pre-flight guidance, see ai-agent-checklist.md
-->

# AGENTS.md — How to Use This Repo Safely

This document is the operating policy for any AI agent consuming the awesome-tech-failures repository.

---

## Core Principles

### This Repo Is Memory, Not Authority

Entries are learning material. They do not replace verification, testing, or human judgment.

- Treat `direct_incident` as higher-confidence than `repeated_pattern`
- Never take destructive actions based only on a summary
- Always verify against primary sources when possible
- Patterns inform decisions; they do not make decisions for you

### Required Behavior for Agents

1. **Verify, don't assume**
   - Check evidence type before weighting decisions
   - Cross-reference patterns with specific incidents
   - Validate that conditions actually match before applying lessons

2. **Require human approval for irreversible actions**
   - If an action is destructive, permanent, or high-impact → require explicit human approval
   - Use the Pre-Flight Checklist before any write access in production
   - Block actions that bypass approval gates

3. **Budget and limit resources**
   - Set hard budgets before agent execution
   - Monitor token/cost usage in real-time
   - Stop execution when limits are approached

4. **Maintain observability**
   - Log all actions with context
   - Keep decision trails for audit
   - Make reasoning visible to humans

---

## Recommended Workflow for Agents

### Mode 1: "I'm About to Do X — What Can Go Wrong?"

1. **Identify planned actions** → Extract tags (write_access, prod, budget, etc.)
2. **Retrieve relevant patterns** → Search by action type and risk profile
3. **Generate risk memo** → Summarize applicable failures and lessons
4. **Apply pre-flight checks** → Run blocking/advisory rules from `agent_preflight.json`
5. **Execute with safeguards** → Set budgets, enable kill switches, require approvals

### Mode 2: "This Incident Is Happening — What Does It Resemble?"

1. **Capture symptoms** → Latency, errors, data issues, user reports
2. **Map to tags** → Extract cause, impact, and category from symptoms
3. **Search entries** → Find analogous incidents by pattern
4. **Return comparable cases** → Include timeline, root cause, and lessons
5. **Suggest investigation paths** → Based on what worked in similar cases

### Mode 3: "Policy Gate Before Tool Call"

Before any tool call, evaluate:

| Condition | Action |
|-----------|--------|
| Write + no rollback | BLOCK |
| Production + no approval | BLOCK |
| Budget < $10 remaining | BLOCK |
| User input in prompt | WARN + sanitize |
| AI output + high impact | Require review |

See `agent/policies/agent_preflight.json` for executable rules.

---

## Data Model for Agents

### Entry Fields (from `agent/entries.ndjson`)

```json
{
  "id": "stable-slug-identifier",
  "title": "Human-readable title",
  "year": 2023,
  "evidence_type": "direct_incident | repeated_pattern",
  "category": "ai-slop | outage | security | startup | product | decision",
  "cause": "human-error | automation | architecture | incentives | ai",
  "stage": "early | growth | scale | decline",
  "impact": ["money", "trust", "users", "data-loss", "morale"],
  "summary": "1-2 sentence description",
  "root_cause": "Short explanation",
  "lessons": ["actionable lesson 1", "actionable lesson 2"],
  "patterns": ["pattern-id-1", "pattern-id-2"],
  "tags": ["free-form", "tags"],
  "sources": [{"title": "Name", "url": "https://...", "kind": "primary"}]
}
```

### Pattern Fields (from `agent/patterns.ndjson`)

```json
{
  "id": "pattern-slug-identifier",
  "title": "Pattern name",
  "description": "What the pattern is",
  "common_tags": ["tag1", "tag2"],
  "related_categories": ["ai-slop", "outage"],
  "examples": ["entry-id-1", "entry-id-2"]
}
```

---

## Pattern-to-Action Mapping

| Pattern | Risk Indicator | Recommended Action |
|---------|---------------|-------------------|
| Automation Without Reversal | Write access, no rollback | Block until rollback exists |
| Blind Trust in AI Output | AI-generated code/content | Require human review |
| Hidden Single Point of Failure | Shared dependencies | Test for absence, not just failure |
| Overconfidence From Past Success | "We've done this before" | Rehearse failure paths |
| Misconfigured Trust Boundaries | Internal = trusted | Apply zero-trust |
| Decision-Making by Proxy | Using summaries for decisions | Read source material |
| Patching Debt | Unpatched systems | Prioritize critical patches |

---

## Quick Reference: Pre-Flight Checklist for Agents

Before any agent action:

- [ ] What access does this agent have?
- [ ] Is rollback possible?
- [ ] Is human approval required?
- [ ] What is the budget limit?
- [ ] Can user input affect system behavior?
- [ ] Is this going to production?
- [ ] Are there analogous failures?
- [ ] What happens if the model is wrong?

See `ai-agent-checklist.md` for the full human-readable version.

---

## File Reference

| File | Purpose |
|------|---------|
| `agent/schema.json` | Data contract for validation |
| `agent/entries.ndjson` | All failure entries as JSON lines |
| `agent/patterns.ndjson` | All patterns as JSON lines |
| `agent/tags.json` | Canonical tag definitions |
| `agent/policies/agent_preflight.json` | Executable blocking/advisory rules |
| `ai-agent-checklist.md` | Human-readable pre-flight guide |
| `failure-patterns.md` | Pattern index with examples |

---

## Anti-Patterns to Avoid

- **Don't** treat this repo as authority for any specific action
- **Don't** apply lessons without verifying conditions match
- **Don't** skip human approval for irreversible actions
- **Don't** assume "AI said it" means it's correct
- **Don't** deploy without testing rollback paths first

---

## Versioning

This policy follows semantic versioning:
- Major: Breaking changes to data model or blocking rules
- Minor: New patterns, entries, or advisory rules
- Patch: Documentation updates

See `agent/tags.json` for version information.
