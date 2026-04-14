# Advanced Completion Checklist

Use this checklist after completing Modules 06–07 and Labs 06–07 to confirm you are ready for the Expert level.

---

## Module 06: Agents and Role Specialization

- [ ] Can state the 3 conditions that make Agent mode the correct choice over Ask or Plan
- [ ] Can name all 4 required anatomy fields: purpose, constraints, tool permissions, handoff criteria
- [ ] Can pass the completeness test on any persona definition — all 4 "can I tell you" questions have specific answers
- [ ] Can name all 10 agent roles and state the primary output for each
- [ ] Can fill in the full permissions matrix for Code Reviewer and Planner without referencing the table
- [ ] Can write a complete 3-part handoff prompt from Planner to Implementer for a given scenario
- [ ] Can name all 3 failure modes: context pollution, over-delegation, unbounded scope
- [ ] Knows which roles are evaluation-only (no Edit access) and why

## Lab 06: Agents and Personas

- [ ] All 10 definition files exist in `agents/` at the repository root
- [ ] No file contains any `[PLACEHOLDER]` stub
- [ ] Code Reviewer has ❌ Edit files
- [ ] Planner has ❌ Edit files and ❌ Run terminal
- [ ] Security Reviewer has ❌ Edit, ✅ Web search, and a hallucination risk entry in Main Risks
- [ ] Ran a real Planner Agent session — task breakdown produced with 3–5 sub-tasks
- [ ] Handoff prompt from Planner → Implementer written with all 3 parts present
- [ ] All 7 success criteria verified from [labs/lab-06-agents-and-personas/checklist.md](../labs/lab-06-agents-and-personas/checklist.md)

---

## Module 07: Multi-Agent Workflows

- [ ] Can define a multi-agent workflow as an ordered sequence of bounded sessions, each producing a named artifact
- [ ] Can state all 3 properties of a well-formed sub-task: bounded scope, single acceptance criterion, no compound steps
- [ ] Can select the correct workflow pattern for Feature Delivery, Bug Investigation, and Refactor and Validate
- [ ] Can write a complete workflow file with all 5 required sections before running any session
- [ ] Can state all 4 workflow failure modes: one-session sprawl, no artifact discipline, skipped review, workflow drift
- [ ] Uses the default model for Planner, Implementer, Code Reviewer, and Test Engineer
- [ ] Knows that all outputs must be committed files — nothing exists only in chat history

## Lab 07: Run a Complete Multi-Agent Workflow

- [ ] `agents/workflow-feature-delivery.md` committed before the first Agent session opened
- [ ] `feature-breakdown.md` committed — 4–6 sub-tasks, each with a named file scope and one acceptance criterion
- [ ] Sub-task 1 implemented and committed in `notifications.py`
- [ ] Code Reviewer session produced a numbered findings document — no source file edits
- [ ] `agents/workflow-feature-delivery.md` `## Outcome` section filled in and committed
- [ ] All 7 success criteria verified from [labs/lab-07-multi-agent-workflow/checklist.md](../labs/lab-07-multi-agent-workflow/checklist.md)

---

## Mindset Check

Before moving to Expert level, confirm these behaviors:

- [ ] I write a workflow file before opening any Agent session — not after
- [ ] I stop a session at the exit condition, not when the agent runs out of new ideas
- [ ] I treat Code Reviewer as a required step, not optional when confident
- [ ] I would not accept a sub-task breakdown that contains "and" connecting two implementation steps
- [ ] I commit every session's output before closing the session

---

## You're Ready for Expert Level

→ [LEARNING_PATH.md — Path 4: Expert](../LEARNING_PATH.md#path-4--expert)
→ Start with [Module 08 — Advanced Features](../modules/08-advanced-features/)
