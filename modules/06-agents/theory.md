# Module 06: Agents and Role Specialization — Theory Reference

> Extended reference for [README.md](./README.md). Read the module overview first.
> Prose sections are capped at 500 words; tables and code blocks are excluded from that limit.

This page extends the README with four topics not covered there: session lifecycle mechanics, monorepo agent strategy, context window management per role, and the cases where agents should not be used at all.

---

## Session Lifecycle Mechanics

An agent session is a bounded execution loop, not a conversation. Understanding the mechanics prevents the most expensive failure mode: running a session past the point where it can produce correct output.

**The lifecycle has four phases:**

1. **Initialization.** The initialization prompt sets role, scope, constraints, tool permissions, and exit condition. This is the only point at which the agent has a clean context. Everything added after initialization competes for the same context window.

2. **Execution.** The agent performs tool calls: reads files, runs terminal commands, creates or edits files. Each tool-call result is added to the context. Context fills in one direction only.

3. **Completion.** The exit condition from the initialization prompt is reached. The deliverable exists. The session stops at this point — not after exploring adjacent concerns.

4. **Handoff.** The 3-part handoff prompt is written while the output is still fresh. This is the only sanctioned way to transfer work between roles without losing decisions or creating duplication.

**What corrupts the lifecycle:** Adding a second role objective during execution. Asking the agent to "also review what it just wrote." Continuing past the exit condition because the session is still responding coherently.

---

## Monorepo Agent Strategy

In a monorepo with multiple distinct areas — API, data layer, frontend, pipeline — agent scope boundaries follow the same logic as `applyTo` globs from Module 05. One session per area per role.

**Pattern: one session per area per role.**

```
Feature: Add notification system
Session 1: Planner    — scope: feature-request.md + docs/architecture.md
Session 2: Implementer — scope: src/notifications.py only
Session 3: Test Engineer — scope: tests/test_notifications.py only
Session 4: Code Reviewer — scope: PR diff (notifications.py + test file)
```

Do not start Session 2 until Session 1's output is a committed file — not a clipboard block. A committed plan becomes a context anchor for every subsequent session. It is readable, version-controlled, and can be referenced by file path rather than pasted into the next session's context.

**What not to do:** Do not start Session 2 with the full output of Session 1 pasted into the initialization prompt. The Implementer does not need the Planner's reasoning — only the task list and acceptance criteria. Pass the file path, not the content.

---

## Context Window Management per Role

Different roles have different context loads. The higher the context load, the smaller the scope must be.

| Role | Context load | Why |
|------|-------------|-----|
| Planner / Analyst | Low | Reads only requirement docs and architecture |
| Implementer | Medium | Source file + spec document |
| Code Reviewer | Medium-High | Source + test file + prior findings |
| Security Reviewer | High | Source + OWASP references + exploit analysis |
| Solution Architect | High | Multiple architecture docs, dependency graph |
| Performance Optimizer | High | Source + profiling data + dependency graph |

A Security Reviewer session spanning 20 files is not more thorough — it is overfull and will miss findings in the last files it reads. A Performance Optimizer session with no scope boundary will profile everything and optimize nothing.

**Rule:** If a role's context load is High, the file scope must be one function or one small module. Split into multiple sessions rather than expanding the scope.

---

## When NOT to Use Agents

| Scenario | Better tool | Reason |
|----------|------------|--------|
| Write one function | Ask mode + structured prompt | One turn, no multi-file dependency |
| Fix a single bug | Inline chat (`Ctrl+I`) | Surgical change; agent adds overhead |
| Explain how a module works | Ask mode | Information retrieval, not execution |
| Draft a docstring for one function | Ask or Inline chat | Language task, resolved in one turn |
| Produce a design without making changes | Plan mode | No tool calls needed |
| Run a security check on one function | Ask mode with security scope prompt | Single-turn output; no file editing needed |

The cost of a wrong tool choice is real: an unnecessary agent session consumes 5–15× the context of an equivalent Ask prompt.

---

## Official Resources

- [Agent mode in VS Code](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)
- [GitHub Copilot agents documentation](https://docs.github.com/en/copilot/concepts/agents)
- [Custom agents in GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
