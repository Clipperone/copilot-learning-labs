# Module 07: Multi-Agent Workflows

> **Level:** Advanced
> **Estimated time:** ~2.5 hours (module theory ~1.5 hrs · lab ~70 min)
> **Prerequisite:** [Module 06 — Agents and Role Specialization](../06-agents/) · All 10 agent definitions must be complete and passing the completeness test in `agents/` before this module.
> **Verified:** 2026-04

> ⚠️ **Premium request note:** The default model handles most workflow roles — Planner, Implementer, Code Reviewer, and Test Engineer. Escalate to Claude or o1 for Solution Architect sessions (system design, ADR authoring) and Security Reviewer sessions (OWASP chain reasoning). Escalating all sessions because one step needed a premium model is the most common premium waste pattern in multi-agent workflows.

---

## Learning Objectives

By the end of this module you will be able to:

1. Define a multi-agent workflow as an ordered sequence of bounded sessions, each producing a named artifact.
2. Decompose a complex task into sub-tasks that respect agent role boundaries and the single-output rule.
3. Write a workflow file before executing any session — documenting sequence, roles, artifacts, and verification gates.
4. Execute the Feature Delivery workflow (Planner → Implementer → Code Reviewer) end-to-end with clean handoffs.
5. Select the correct workflow pattern for a given problem type: feature delivery, bug investigation, or refactor and validate.
6. Identify and interrupt the 4 workflow failure modes before they waste premium requests.

---

## Why This Module Exists

Module 06 defined 10 specialized agent roles and proved each role should have a bounded scope and a named exit condition. One gap remained: what to do when the work is larger than any single role's scope.

A **multi-agent workflow** closes that gap. It is an ordered sequence of bounded sessions where each role operates within its lane, produces a named artifact, and hands off to the next role using the 3-part prompt from Module 06. The context window resets at every handoff. Each session is independently reviewable. Nothing is permanently delegated to a single open-ended session that accumulates everything.

This module teaches you to design, document, and execute these workflows — and to write the workflow file before opening the first Agent session.

---

## What Is a Multi-Agent Workflow?

A multi-agent workflow has four properties:

1. An **ordered sequence** of bounded agent sessions.
2. Each session produces exactly one **named artifact** — a committed file.
3. Each session **hands off** to the next using the 3-part prompt from Module 06.
4. The workflow is **documented before execution** in a workflow file.

The critical difference from a long single session: a workflow resets the context window at every role boundary. Planner artifacts do not occupy the Implementer's context. Reviewer findings do not restate the implementation. Each role starts clean with only what it needs.

**What a workflow is not:**

| Anti-pattern | Why it fails |
|--------------|-------------|
| One long Agent session covering all roles | Context accumulates; early decisions crowd later turns; no clean role boundary is possible |
| Asking the Implementer to also review its own code | Evaluation and implementation conflict; the Implementer cannot evaluate its own work objectively |
| Running sessions without a workflow file | No verification gate; no repeatable record; no way to pause and resume cleanly |
| Writing the workflow file after the run as documentation | A workflow file is a guide, not a transcript — it must exist before the first session opens |

---

## Task Decomposition

Every multi-agent workflow begins with decomposition: breaking the original problem into sub-tasks that individual agent sessions can handle without scope drift.

**A well-formed sub-task has exactly 3 properties:**

| Property | Definition | Violation |
|----------|-----------|-----------|
| **Bounded scope** | Names one or two specific files and one function or feature area | "Update the data layer" — no file named |
| **Single acceptance criterion** | One measurable condition that proves the sub-task is complete | "Implement and test the handler" — two criteria |
| **No compound steps** | The description contains no "and" connecting two independent actions | "Add the endpoint and update the README" — split required |

**Sizing rule:** If a sub-task requires more than one agent role to complete, it is too large. Split it.

**Decomposition failure modes:**

| Failure | Symptom | Fix |
|---------|---------|-----|
| Too coarse | Implementer modifies 5+ files in one session | Return to Planner; tighten the scope to one file |
| Too fine | 15+ sub-tasks with 2-line implementations each | Merge sub-tasks that belong to the same role and file |
| Role-scope violation | Planner breakdown includes implementation instructions | Remove all "how" from planning artifacts; keep only "what" and "acceptance criterion" |

---

## Three Workflow Patterns

These three patterns cover the most common professional development scenarios. Each is a proven sequence of roles, artifacts, and handoffs. Learn the sequence — do not improvise a custom order until you have run each pattern at least once.

---

### Pattern 1 — Feature Delivery

Use when: delivering a new feature from a written specification or user story.

| Step | Role | Input | Output artifact |
|------|------|-------|-----------------|
| 1 | Planner | Feature request document | `feature-breakdown.md` — sub-tasks with scope and acceptance criteria |
| 2 | Solution Architect *(if needed)* | Feature breakdown | Architecture note or ADR |
| 3 | Implementer | Feature breakdown — one sub-task only | Working code, committed |
| 4 | Code Reviewer | Implementation diff | Numbered findings document |
| 5 | Test Engineer *(if tests not in step 3)* | Implementation | Test suite, passing |

Repeat steps 3–5 for each remaining sub-task. Do not batch multiple sub-tasks into one Implementer session.

**When to skip the Architect step:** Skip when the feature does not introduce new components, cross-service dependencies, or data model changes.

---

### Pattern 2 — Bug Investigation

Use when: a bug is reported but the root cause is unknown.

| Step | Role | Input | Output artifact |
|------|------|-------|-----------------|
| 1 | Planner / Analyst | Bug report, reproduction steps | Root-cause hypothesis document |
| 2 | Implementer | Root-cause document, specific file and function scope | Fix, committed |
| 3 | Test Engineer | Fix + original bug description | Regression test, passing |
| 4 | Code Reviewer | Fix diff | Findings — confirm no new issues introduced |

**If the hypothesis is wrong:** If the Implementer cannot reproduce the bug using the hypothesis, close the session without modification. Return to Analyst with new evidence before opening a new Implementer session.

---

### Pattern 3 — Refactor and Validate

Use when: improving internal structure with no behavior change.

| Step | Role | Input | Output artifact |
|------|------|-------|-----------------|
| 1 | Refactoring Specialist | File or module, stated refactoring goal | Refactored code — no behavior change |
| 2 | Test Engineer | Refactored code + original test suite | Passing tests confirming no regression |
| 3 | Code Reviewer | Refactored diff + test results | Findings — structure improved, behavior preserved |

**Constraint:** The Refactoring Specialist must not add features or fix unrelated bugs in the same session. One objective per session.

**If there are no existing tests:** Add a Test Engineer step before the Refactoring Specialist to baseline the behavior first.

---

## Workflow Documentation

Write the **workflow file** before executing any session. It is a plan, not a log.

**Required sections:**

| Section | Contents |
|---------|---------|
| `## Pattern` | Feature Delivery, Bug Investigation, or Refactor and Validate |
| `## Problem statement` | One paragraph: what the problem is and what constitutes a successful outcome |
| `## Steps` | Numbered list: role, input artifact, output artifact, file scope, verification gate |
| `## Active context` | Active instruction file path; any architecture decisions that persist across sessions |
| `## Outcome` | Filled in after completion: actual artifacts, deviations from plan, issues found |

The workflow file lives in `agents/`. Name it `workflow-[purpose].md` — for example `workflow-feature-delivery.md` or `workflow-bug-login.md`.

The `## Active context` section is not optional. Without it, every initialization prompt must reconstruct project context from scratch. State it once in the workflow file and copy it into every handoff prompt's carry-forward block.

---

## Context Hygiene at Workflow Level

Module 06 covered context hygiene within a session. Workflows introduce cross-session hygiene — keeping information clean across multiple role boundaries.

**Rules:**

1. **One role per session.** Do not continue a Planner session into implementation.
2. **All artifacts are committed files.** If output exists only in the chat history, it does not exist. Commit before closing.
3. **The handoff prompt is the only bridge.** Nothing else transfers between sessions reliably.
4. **Carry-forward is always explicit.** State the active instruction file path in every initialization prompt — do not assume it persists.

| What transfers across sessions | What does not |
|-------------------------------|---------------|
| Named artifact files (committed to the repository) | Conversation history |
| Active instruction file (stated explicitly in the handoff) | In-context decisions made verbally mid-session |
| Architecture decisions in a committed ADR | Context window content from prior sessions |
| Key constraints copied verbatim into the initialization prompt | Implicit understanding built over multiple turns |

---

## Workflow Failure Modes

| Failure mode | What it looks like | Safeguard |
|-------------|-------------------|-----------|
| **One-session sprawl** | A single session handles plan, implementation, and review without stopping | End the session at role completion; write a handoff prompt before opening the next |
| **No artifact discipline** | Session output exists only in chat history; nothing is committed | Every session closes with a committed file — no exceptions |
| **Skipped review** | Implementer output goes to merge without a Code Reviewer pass | Code Reviewer is a required step in every Feature Delivery workflow |
| **Workflow drift** | The workflow file is modified mid-run to remove steps that became inconvenient | Keep the original plan; record deviations in `## Outcome` instead of rewriting the plan |

---

## Exercises

See [exercises.md](./exercises.md) for full instructions.

**Quick list:**

1. **Decompose for a workflow** — Read a feature request and produce a valid sub-task breakdown with scope boundaries and acceptance criteria.
2. **Match pattern to problem** — Given 5 scenarios, select the correct workflow pattern and justify the choice.
3. **Spot the decomposition failure** — Review a broken sub-task list, identify all violation types, and rewrite the broken sub-tasks.
4. **Write a workflow file** — Produce a complete `workflow-feature-delivery.md` for a given feature request before running any session.
5. **Write the Bug Investigation handoff chain** — Write all three 3-part handoff prompts for the Bug Investigation pattern end-to-end.

---

## Common Mistakes

| Mistake | Why it happens | How to fix it |
|---------|---------------|---------------|
| One long session instead of separate role sessions | Feels faster; requires less setup | End the session when the role's deliverable exists; write a handoff prompt; open a new session |
| Workflow file written after the run | Treated as documentation rather than a guide | Write the workflow file in full before opening the first Agent session |
| Skipping the Code Reviewer | Confident the implementation is correct | Code Reviewer is not optional — it catches issues the Implementer cannot see about its own output |
| Planner session continues past the sub-task list | No exit condition enforced | Stop the Planner session immediately when the sub-task list is complete |
| In-context decisions passed across sessions verbally | Assuming chat context persists between sessions | All decisions that must persist must live in a committed file referenced in the handoff prompt |
| All roles escalated to a premium model | One session needed it so all should | Default model handles Planner, Implementer, Reviewer, Test Engineer; escalate only Architect and Security Reviewer |

---

## Token and Premium Request Impact

| Action | Cost level | Notes |
|--------|-----------|-------|
| Writing a workflow file | Low | Use Plan or Ask mode — no Agent session needed |
| Planner session | Low–Medium | Default model; decomposition does not require deep reasoning |
| Implementer session | Medium | Default model handles most feature work |
| Code Reviewer session | Low–Medium | Pattern matching and rule checking — default model sufficient |
| Solution Architect session | High | Escalate to Claude or o1; system design benefits from extended reasoning |
| Security Reviewer session | High | Escalate; OWASP chain reasoning is premium-justified |

---

## Completion Criteria

You have completed this module when you can:

- [ ] Explain the difference between a multi-agent workflow and a single long session.
- [ ] State all 3 properties of a well-formed sub-task and rewrite a broken one.
- [ ] Select the correct workflow pattern for a feature, bug, and refactor scenario.
- [ ] Write a complete workflow file before running any session.
- [ ] Write all 3-part handoff prompts for the Feature Delivery pattern transitions.
- [ ] Name all 4 workflow failure modes and state the safeguard for each.

See [checklist.md](./checklist.md) for the full self-assessment.

---

## Files in This Module

| File | Purpose |
|------|---------|
| `README.md` | Module overview (this file) |
| `theory.md` | Extended reference — artifact design, decomposition matrix, workflow file anatomy |
| `exercises.md` | All 5 exercises with full instructions and expected answers |
| `checklist.md` | Completion checklist and self-assessment |

---

## Paired Lab

[Lab 07 — Run a Complete Multi-Agent Workflow](../../labs/lab-07-multi-agent-workflow/) — execute the Feature Delivery pattern end-to-end in real Agent sessions.

---

## Next Module

[Module 08 — Advanced Features](../08-advanced-features/) · Complete Module 07 and pass checklists/advanced-completion.md *(coming soon)* before advancing.

Module 07 taught you to orchestrate roles manually: one initialization prompt per session, one handoff prompt between each step. Module 08 introduces Plan mode, terminal integration, and CI/CD connections that automate the mechanics you just learned to do explicitly.
