# Module 06 — Completion Checklist

Use this checklist after finishing the module reading and all 5 exercises, and before starting Lab 07. If you cannot check an item confidently, revisit the linked section in [README.md](./README.md).

---

## What Is an Agent Session?

- [ ] I can state the 3 conditions that make Agent mode the correct choice over Ask, Edit, or Plan.
- [ ] I can apply the cost test — "Could a structured Ask prompt produce the same result?" — and give the answer that justifies using an agent.
- [ ] I know why agent sessions are more expensive than Ask mode and can name two specific reasons.

## Agent Anatomy

- [ ] I can name all 4 required fields: purpose, constraints, tool permissions, handoff criteria.
- [ ] I can pass the completeness test by answering all four "can I tell you" questions about any persona I read.
- [ ] I can rewrite a vague purpose statement as a single sentence naming what the role produces.
- [ ] I know that a persona without handoff criteria has no exit condition and will run until context fills.

## The 10 Agent Roles

- [ ] I can name all 10 roles without looking them up.
- [ ] I can state the primary output for each role — what a successful session produces.
- [ ] I know which roles have write access (✅) and which are read-only (❌) — and why evaluation roles are always read-only.

## Tool Permissions Model

- [ ] I can fill in the full permissions matrix for the Code Reviewer and Planner roles without referencing the table.
- [ ] I can write a one-sentence justification for why each ❌ entry is ❌ rather than ✅.
- [ ] I know what ⚠️ means and can give an example of a conditional permission for Solution Architect.

## Handoff Criteria and the Handoff Prompt

- [ ] I can state the 3 parts of a handoff prompt: (1) what was produced, (2) next role's objective, (3) carry-forward constraints.
- [ ] I know the handoff must scope the next role to a single sub-task, not a multi-task sequence.
- [ ] I can write a Planner → Implementer handoff for a given scenario without referencing the template.

## Risks and Safeguards

- [ ] I can name all 3 failure modes: context pollution, over-delegation, unbounded scope.
- [ ] I can identify which failure mode is operating from a session description and quote the evidence.
- [ ] I know the session discipline rule: one role, one scoped objective, ≤ 45 minutes of active turns.
- [ ] I know the 4 signals that a session should stop — and what each means.

## Premium Model Decisions

- [ ] I know which roles justify a premium model: Security Reviewer — and sometimes Solution Architect and Performance Optimizer.
- [ ] I know which roles do not justify a premium model and can state why.

---

## Ready for Lab 07?

All items above checked → proceed to [Lab 07 — Define and Run Your First Agent Session](../../labs/lab-07-first-agent-session/).

Not all items checked → return to [exercises.md](./exercises.md) for the concept you want to reinforce.
