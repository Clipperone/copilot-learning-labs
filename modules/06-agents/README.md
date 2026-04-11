# Module 06: Agents and Role Specialization

> **Level:** Advanced
> **Estimated time:** ~3 hours (module theory ~2 hrs · lab ~60 min)
> **Prerequisite:** [Level 2 complete](../../SYLLABUS.md#level-2--intermediate) (Modules 01–05) · Module 05 in particular. Agent personas apply the same 4 design principles as instruction files — both must be solid before agent work.
> **Verified:** 2026-04

> ⚠️ **Premium request note:** Most agent sessions run well on the default model. Escalate to Claude or o1 for Security Reviewer sessions (exploit-path reasoning) and Solution Architect sessions (multi-step system design). A common waste pattern is opening a premium model session for a task that a structured Ask prompt would handle.

---

## Learning Objectives

By the end of this module you will be able to:

1. Explain what an agent session is and state the 3 conditions that make it the correct mode over Ask, Edit, or Plan.
2. Design a role-based persona using the 4-field agent anatomy: purpose, constraints, tool permissions, handoff criteria.
3. Write a valid initialization prompt for each of the 10 core agent roles without referencing their definition files.
4. Build a tool permissions matrix (✅ Allow / ⚠️ Conditional / ❌ Deny) for any agent role and justify each boundary.
5. Write a 3-part handoff prompt that closes one role session and opens the next without context leakage.
6. Recognize the 3 failure modes — context pollution, over-delegation, unbounded scope — and intervene before they waste requests.

---

## Why This Module Exists

Module 05 taught you to encode project conventions using 4 design principles: specific, imperative, bounded, non-contradictory. An agent persona applies the same 4 principles to a **role** rather than an instruction file.

There is one critical addition. An instruction file has no concept of completion — it runs indefinitely. An agent persona must specify **when the session ends**. A persona without an exit condition is a session that keeps running until the context window fills and output degrades.

This module teaches you to define personas that start cleanly, execute a bounded objective, and hand off — not drift.

---

## What Is an Agent Session?

Agent mode is the only Copilot mode that can hold tool calls, run multiple turns, and maintain a working loop across files. It is also the most expensive mode to run incorrectly.

**Use Agent mode when all three conditions are true:**

1. The task spans multiple files or requires tool calls (terminal, file system, test runner).
2. The output cannot be determined in a single turn.
3. The role has a defined deliverable and a named exit condition.

**Use Ask, Edit, or Plan instead when:**

| Condition | Better mode |
|-----------|-------------|
| Single file, single change | Edit |
| Design, plan, or diagnosis — no code changes | Plan or Ask |
| The task has a one-turn prose answer | Ask |
| Inline completion is sufficient | Inline |

**The cost test:** If you could produce the same result with a structured prompt in Ask mode, you do not need an agent session. Agent sessions consume context faster, accumulate tool-call overhead, and are harder to review.

---

## The 10 Agent Roles

The course defines 10 specialized roles. Each has a definition file in `agents/` that you will write in Lab 07.

| Role | Scope | Primary output | File write access |
|------|-------|----------------|------------------|
| Planner / Analyst | Feature / epic | Task breakdown, risk list, acceptance criteria | ❌ |
| Solution Architect | Module / system | Architecture document, ADR, component boundaries | ⚠️ docs only |
| Implementer / Developer | Function / module | Working, tested code aligned to spec | ✅ |
| Refactoring Specialist | File / module | Restructured code with no behavior change | ✅ |
| Code Reviewer | PR / module | Numbered findings: severity, location, suggested fix | ❌ |
| Security Reviewer | Function / file | OWASP findings, exploit paths, remediation | ❌ |
| Test Engineer | Function / module | Test suite with boundary and failure cases | ✅ |
| Documentation Writer | File / module | Docstrings, README sections, ADR | ⚠️ docs only |
| Performance Optimizer | Function / module | Profiled hotspots, optimized implementations | ✅ |
| DevOps / Release Assistant | Repo / pipeline | CI configuration, deploy scripts, task automation | ⚠️ infra only |

**Key rule:** Roles that **evaluate** code — Planner, Code Reviewer, Security Reviewer — never write to source files. Evaluation roles produce text; implementation roles produce code.

---

## Agent Anatomy

Every persona definition requires exactly 4 fields. A missing field makes the persona incomplete and the session unpredictable.

| Field | Required? | What it contains |
|-------|-----------|--------------------|
| **Purpose** | Always | One sentence: what this role produces and for whom |
| **Constraints** | Always | What must NOT happen in this session — explicit prohibitions |
| **Tool permissions** | Always | ✅ / ⚠️ / ❌ for each capability |
| **Handoff criteria** | Always | At least one named condition that signals the session is complete |

**Completeness test:** Read the persona aloud. Can you answer: "What does it produce?", "What is it not allowed to do?", "Which tools can it use?", and "How do I know it's done?" If any answer is "I don't know," that field is incomplete.

### Example — the Planner persona

```
Purpose: Decompose a feature request into bounded, implementation-ready sub-tasks
         with acceptance criteria.

Constraints:
- Do not write code or pseudocode.
- Do not propose implementations — only tasks and acceptance criteria.
- Read only the feature description and existing documentation. Do not open source files.

Tool permissions:
- Read files:    ✅ (feature docs, architecture docs only)
- Edit files:    ❌
- Run terminal:  ❌
- Create files:  ⚠️ (task breakdown document only)
- Web search:    ❌

Handoff criteria:
- All sub-tasks have an acceptance criterion and a scope boundary.
- Hand off to: Implementer when the task breakdown document is committed.
```

---

## Tool Permissions Model

Permissions prevent sessions from taking actions outside their role. Set them in the initialization prompt, not mid-session.

| Role | Read | Edit | Terminal | Create | Web |
|------|:----:|:----:|:--------:|:------:|:---:|
| Planner / Analyst | ✅ | ❌ | ❌ | ⚠️ | ❌ |
| Solution Architect | ✅ | ⚠️ | ❌ | ⚠️ | ✅ |
| Implementer / Developer | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Refactoring Specialist | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Code Reviewer | ✅ | ❌ | ❌ | ⚠️ | ❌ |
| Security Reviewer | ✅ | ❌ | ❌ | ⚠️ | ✅ |
| Test Engineer | ✅ | ✅ | ✅ | ✅ | ❌ |
| Documentation Writer | ✅ | ⚠️ | ❌ | ✅ | ⚠️ |
| Performance Optimizer | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| DevOps / Release Assistant | ✅ | ⚠️ | ✅ | ✅ | ✅ |

⚠️ = conditional — permitted only for files within the stated scope of the session.

**Why this matters:** Every permission granted is a permission the agent may exercise on tools you cannot undo. Reviewer and Planner roles that cannot edit source files produce the same findings quality with zero risk of unintended changes.

---

## Handoff Criteria and the Handoff Prompt

A handoff is not just closing a session — it is a structured transfer where this role's output becomes the next role's input.

**The 3-part handoff prompt:**

```
1. Summary:   [What this role produced — specific files, decisions, deliverables]
2. Objective: [The single bounded task the next role must accomplish]
3. Carry-forward: [Active instruction files, architecture decisions, constraints that persist]
```

**Example — Planner → Implementer handoff:**

```
Summary: The Planner produced a task breakdown for the notification system feature.
Three sub-tasks in feature-plan.md: (1) add EventType enum, (2) implement log_event(),
(3) wire into user CRUD handlers. Each has acceptance criteria.

Objective: Implementer — implement sub-task 1: add EventType enum to notifications.py.
Scope: notifications.py only. Do not modify user.py, auth.py, or any other file.

Carry-forward:
- Active instruction file: .github/copilot-instructions.md (type annotations, Google
  docstrings, pytest).
- No MD5 or plain hashing in any code path.
- Complete sub-task 1 only. Stop and signal completion before moving to sub-task 2.
```

**Why separate sessions per sub-task?** Each new session starts with a clean context window. A session that carries Planner output, then Implementer code, then Reviewer findings fills the context window with artifact from previous roles the current role cannot act on. Start clean; hand off early.

---

## Risks and Safeguards

### Context Pollution

**What it is:** A session accumulates output from multiple roles without clearing between them. Planner notes, Implementer code, and Reviewer findings pile up in one session.

**Signs:** Session output gets longer while the specific task does not progress. The agent restates conclusions from earlier turns instead of acting on them.

**Safeguard:** One role per session. End the session when the role's deliverable is complete. Open a new session for the next role using the 3-part handoff prompt.

---

### Over-Delegation

**What it is:** Asking a single session to fulfill multiple role objectives in sequence — plan, implement, review, document — without separating sessions.

**Signs:** The initialization prompt contains more than one role-level objective. The session runs past 45 minutes of active turns. Output contains phrases like "Now switching to implementation…"

**Safeguard:** Read the initialization prompt aloud. If it names two role-level objectives, split it into two sessions before starting.

---

### Unbounded Scope

**What it is:** An agent session with no stated file scope, no exit condition, and no deliverable specification.

**Signs:** The agent modifies files not mentioned in the initialization prompt. Output requests permission to "also update" adjacent files or modules.

**Safeguard:** Every initialization prompt must contain a scope statement: "This session covers `src/notifications.py` only. Do not modify any other file."

---

## Session Length Discipline

Rule: **one role · one scoped objective · ≤ 45 minutes of active turns.**

| Signal | Interpretation | Action |
|--------|---------------|--------|
| Output is longer than the prior three turns combined | Context is accumulating faster than progressing | Stop; write handoff prompt; open new session |
| Agent re-explains decisions made two turns ago | Context window is crowding out working memory | Stop immediately |
| Agent suggests changes outside the stated scope | Scope has drifted | Decline; end session; add scope boundary to new session's init prompt |
| Task still incomplete after 45 min | Under-scoped or over-complex | Stop; split the task; restart |

---

## Initialization Prompt Pattern

Every session opens with the same structure:

```
Role: Act as [ROLE NAME].
Purpose: [ONE-SENTENCE statement of what this session must produce]
Scope: [Exactly which files, functions, or features this session covers]

Constraints:
- [What this role must NOT do]
- [What must not change]
- [What carries forward from prior sessions]

Tool permissions: [State what is and is not permitted]

Exit condition: [Exactly what signals this session is complete — a file, a list, passing tests]
```

The initialization prompt is not optional — it is what separates a scoped agent session from an open-ended chat.

**Example — Security Reviewer session:**

```
Role: Act as a Security Reviewer specializing in Python web applications.
Purpose: Review hash_password() in src/api/auth.py for OWASP A02:2021 vulnerabilities.
Scope: src/api/auth.py — the hash_password() function only.

Constraints:
- Do not edit any file.
- Do not review any function other than hash_password().
- Describe the exploit path before proposing any fix.

Tool permissions:
- Read files: ✅
- Edit files: ❌
- Run terminal: ❌
- Create files: ⚠️ (findings summary only)
- Web search: ✅ (OWASP references only)

Exit condition: A findings document exists with: vulnerability name, OWASP category,
exploit path, recommended fix, and one code line showing the corrected call.
```

---

## Common Mistakes

| Mistake | Root cause | Fix |
|---------|------------|-----|
| Agent mode for a single-turn task | "Agent is more capable" reasoning | Use Ask or Edit; agents add startup overhead and context cost without benefit on bounded tasks |
| Vague initialization: "Act as a senior developer" | Carrying M04 bad habits into persona design | Apply the 4-field anatomy; a persona without exit conditions never terminates cleanly |
| Running Planner + Implementer + Reviewer in one session | "More efficient to keep context" | Context pollution; use separate sessions with 3-part handoff prompts |
| No exit condition in the persona definition | Forgetting that sessions do not self-terminate | Every definition needs at least one named handoff criterion |
| Repeating instruction file rules in the init prompt | Not knowing `.github/copilot-instructions.md` is inherited | Reference the file in the carry-forward block; never duplicate its content |
| Premium model for every agent session | "Premium always performs better" | Default is sufficient for Implementer (routine), Reviewer, Test Engineer, Docs Writer |
| Adding more instructions to fight session drift | Treating drift as an under-instruction problem | Close the session; start fresh with a 3-part handoff prompt |

---

## Premium Model Decision — Role by Role

| Role | Recommended model | Reason |
|------|------------------|--------|
| Planner / Analyst | Default | Task decomposition is within default capability |
| Solution Architect | Claude or GPT-4o | Multi-step system design benefits from depth |
| Implementer / Developer | Default (routine) / GPT-4o (complex algorithms) | Escalate only when default demonstrably fails |
| Refactoring Specialist | Default | Structural analysis — pattern matching |
| Code Reviewer | Default | Finding identification, not causal reasoning |
| Security Reviewer | o1 or Claude | Exploit-path analysis requires multi-step causal reasoning |
| Test Engineer | Default | Mechanical coverage expansion |
| Documentation Writer | Default | Language generation |
| Performance Optimizer | GPT-4o or Claude | Profiling and optimization benefit from multi-step reasoning |
| DevOps / Release Assistant | Default | Configuration generation |

**Rule:** Escalate to a premium model only when the task requires multi-step causal reasoning that the default model demonstrably cannot complete correctly. Try default first.

---

## Exercises

Hands-on exercises are in [exercises.md](./exercises.md).

The paired lab is [Lab 07 — Define and Run Your First Agent Session](../../labs/lab-07-first-agent-session/).

---

## Further Reading

- [theory.md](./theory.md) — Session lifecycle mechanics, monorepo agent strategy, context window management per role, when NOT to use agents
- [agents/](../../agents/) — Agent definition files (populated during Lab 07)
- [templates/agent-definition-template.md](../../templates/agent-definition-template.md) — Authoring standard for all 10 persona definitions
- `.github/copilot-instructions.md` — Active instruction file inherited by every agent session in this repository
- **Multi-agent connection:** The 10 definitions in `agents/` are Module 07's direct prerequisite. Module 07 teaches how to chain roles in coordinated workflows — not redefine them. A workflow is only as bounded as the weakest persona definition it uses.
- **Next:** [Module 07 — Multi-Agent Workflows](../07-multi-agent-workflows/)

---

## Completion Checklist

→ [checklist.md](./checklist.md)
