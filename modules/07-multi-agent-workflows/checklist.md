# Module 07: Multi-Agent Workflows — Completion Checklist

Use this checklist to self-assess before starting [Lab 07](../../labs/lab-07-multi-agent-workflow/).

---

## What Is a Multi-Agent Workflow?

- [ ] I can define a multi-agent workflow as an ordered sequence of bounded sessions, each producing a named artifact.
- [ ] I can state the 4 properties that distinguish a workflow from a long single session.
- [ ] I can identify at least 3 anti-patterns that look like workflows but are not.

---

## Task Decomposition

- [ ] I can state all 3 properties of a well-formed sub-task: bounded scope, single acceptance criterion, no compound steps.
- [ ] I can identify a sub-task that is too coarse and split it correctly.
- [ ] I can identify a sub-task that is too fine and merge it appropriately.
- [ ] I can apply the sizing rule: if a sub-task requires more than one role, it is too large.

---

## Three Workflow Patterns

- [ ] I can state the role sequence for the Feature Delivery pattern without looking it up.
- [ ] I can state the role sequence for the Bug Investigation pattern without looking it up.
- [ ] I can state the role sequence for the Refactor and Validate pattern without looking it up.
- [ ] I can select the correct pattern for a given scenario and justify the choice.
- [ ] I know when to add the Solution Architect step to Feature Delivery and when to skip it.
- [ ] I know what to do when an Analyst hypothesis turns out to be wrong mid-session.

---

## Workflow Documentation

- [ ] I write the workflow file before opening any Agent session — not after.
- [ ] I can produce a complete workflow file with all 5 required sections.
- [ ] I know why `## Active context` is not optional.
- [ ] I name workflow files using the pattern `workflow-[purpose].md` in `agents/`.

---

## Context Hygiene

- [ ] I can state what transfers across session boundaries and what does not.
- [ ] I commit every session's output as a file before closing the session.
- [ ] I state the active instruction file path explicitly in every initialization prompt.
- [ ] I understand why in-context verbal decisions do not persist across sessions.

---

## Workflow Failure Modes

- [ ] I can name all 4 workflow failure modes: one-session sprawl, no artifact discipline, skipped review, workflow drift.
- [ ] I can state the safeguard for each failure mode.
- [ ] I stop a Planner session as soon as the sub-task list is complete.
- [ ] I treat the Code Reviewer step as required — not optional when confident.

---

## Premium Request Optimization

- [ ] I use the default model for Planner, Implementer, Code Reviewer, and Test Engineer.
- [ ] I escalate to a premium model only for Solution Architect and Security Reviewer sessions.
- [ ] I use Plan or Ask mode to write a workflow file — not Agent mode.

---

## Ready for Lab 07?

If all checkboxes above are checked, proceed to [Lab 07 — Run a Complete Multi-Agent Workflow](../../labs/lab-07-multi-agent-workflow/).

If any section is incomplete, re-read the corresponding section in [README.md](./README.md) or [theory.md](./theory.md) before starting the lab.
