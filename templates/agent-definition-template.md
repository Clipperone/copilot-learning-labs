# Agent / Persona: [NAME]

> **Role category:** planner | architect | implementer | refactoring | reviewer | security | testing | documentation | performance | devops
> **Scope:** single file | module | feature | full project
> **Session type:** short (< 30min) | medium (30–90min) | long (> 90min)
> **Verified:** YYYY-MM

---

## Purpose

[One paragraph: what this agent role is for, what perspective it takes, and what unique value it adds compared to using Copilot without a persona.]

---

## When to Use

- [Situation 1 that triggers this agent]
- [Situation 2]
- [Situation 3]

**Do not use when:** [Situation where this agent is the wrong choice — and what to use instead.]

---

## Ideal Starting Prompt

```
[Paste the exact prompt that initializes this agent's context and persona.
Include: role, constraints, what it should NOT do, expected output format.]
```

---

## Suggested Tool Permissions

| Tool / Capability | Allow | Notes |
|-------------------|-------|-------|
| Read files | ✅ | Required |
| Edit files | ✅ / ⚠️ / ❌ | [Condition or restriction] |
| Run terminal commands | ✅ / ⚠️ / ❌ | [Condition or restriction] |
| Create new files | ✅ / ⚠️ / ❌ | [Condition or restriction] |
| Web search / browse | ✅ / ⚠️ / ❌ | [Condition or restriction] |

---

## Expected Outputs

By the end of a session with this agent, you should have:

- [ ] [Output 1 — a document, a set of files, a checklist, a refactored module]
- [ ] [Output 2]
- [ ] [Output 3]

---

## Main Risks

| Risk | Mitigation |
|------|-----------|
| [Risk 1 — e.g., hallucinates non-existent APIs] | [How to guard against it] |
| [Risk 2 — e.g., scope creep] | [How to guard against it] |

---

## Completion / Handoff Criteria

Consider this agent's session complete when:

- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Hand off to:** [Agent name](./agent-name.md) when [condition — e.g., "planning is done and implementation is ready to start"].

---

## Handoff Example

**From:** [This agent]
**To:** [Next agent]
**Trigger:** [What signals the handoff]

**Handoff prompt:**

```
[Exact prompt to start the next agent, including a summary of what this agent produced]
```

---

## Related Modules

- [Module XX — Title](../modules/XX-title/)

## Related Workflow

- [Workflow name](../agents/README.md#workflow-name)
