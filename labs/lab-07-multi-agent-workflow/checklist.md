# Lab 07 — Completion Checklist

Use this checklist after completing all 5 tasks. If you cannot check an item, return to the task that produced it.

---

## Task 1 — Workflow File

- [ ] `agents/workflow-feature-delivery.md` exists at the repository root
- [ ] The file was committed before the Planner session in Task 2 (check `git log`)
- [ ] `## Pattern` is filled in as "Feature Delivery"
- [ ] `## Problem statement` is one paragraph: problem, success definition, out-of-scope items
- [ ] `## Active context` references `.github/copilot-instructions.md` by path
- [ ] `## Steps` has at least 4 steps, each with a named role, input, output filename, scope, and verification gate
- [ ] `## Outcome` is present as a template (not yet filled in at this point)

---

## Task 2 — Planner Session

- [ ] I ran a real Agent mode session using `agents/planner.md`
- [ ] `feature-breakdown.md` is committed before the Implementer session
- [ ] Every sub-task in `feature-breakdown.md` names at least one specific file
- [ ] Every sub-task has exactly one acceptance criterion
- [ ] No sub-task contains "and" connecting two independent implementation steps
- [ ] I stopped the session when the breakdown was complete — I did not continue into architecture or implementation

---

## Task 3 — Implementer Session

- [ ] I wrote a 3-part Planner → Implementer handoff prompt before opening the new session
- [ ] The handoff prompt Part 3 (carry-forward) references `.github/copilot-instructions.md`
- [ ] The handoff prompt explicitly lists files that must not be modified
- [ ] The Implementer session was scoped to sub-task 1 only
- [ ] The implementation is committed to the correct file
- [ ] No file outside the sub-task 1 scope was modified (`git diff` confirms)
- [ ] The acceptance criterion from the breakdown is met

---

## Task 4 — Code Reviewer Session

- [ ] I wrote a 3-part Implementer → Code Reviewer handoff prompt before opening the new session
- [ ] The handoff prompt explicitly states the Reviewer must not modify any file
- [ ] The Reviewer session produced numbered findings — not inline code edits
- [ ] Each finding is marked BLOCKING or NON-BLOCKING
- [ ] `review-findings.md` is committed
- [ ] No source file was modified during the Reviewer session

---

## Task 5 — Workflow File Updated

- [ ] `agents/workflow-feature-delivery.md` `## Outcome` section is filled in with real content
- [ ] Artifacts produced are listed with their committed paths
- [ ] Any deviations from the original plan are recorded (or "none" if none occurred)
- [ ] BLOCKING findings from the Reviewer are noted and their resolution status is stated
- [ ] The updated workflow file is committed

---

## Workflow Integrity Check

- [ ] A team member reading `agents/workflow-feature-delivery.md` alone could identify what was done, what was produced, and what issues remain
- [ ] All 4 expected output files exist in the repository
- [ ] Every commit made during this lab has a clear message identifying which task produced it

---

## Common Mistakes Summary

- [ ] I wrote the workflow file before opening the first Agent session — not after
- [ ] I did not ask the Code Reviewer to fix the issues it found
- [ ] I treated the exit condition as a real stopping point, not a suggestion

---

## Completed?

If all checkboxes above are checked, proceed to [checklists/advanced-completion.md](../../checklists/advanced-completion.md) to complete Level 3.
