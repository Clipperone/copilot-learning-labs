# Lab 06 — Completion Checklist

Use this checklist after completing all 4 tasks. If you cannot check an item, return to the task that produced it.

---

## Task 1 — Agent Definitions (3 core roles)

- [ ] `agents/planner.md` exists and all 4 anatomy fields are filled in
- [ ] `agents/implementer.md` exists and all 4 anatomy fields are filled in
- [ ] `agents/code-reviewer.md` exists and all 4 anatomy fields are filled in
- [ ] No file contains any `[PLACEHOLDER]` stub from the template
- [ ] Planner has ❌ for Edit files and ❌ for Run terminal
- [ ] Code Reviewer has ❌ for Edit files
- [ ] Each definition passes the completeness test: all 4 "can I tell you" questions have specific answers

## Task 2 — Planner Session

- [ ] I ran a real Agent mode session using my Planner initialization prompt
- [ ] The session produced a task breakdown with 3–5 sub-tasks
- [ ] Each sub-task has exactly one acceptance criterion
- [ ] Each sub-task names at least one file it affects
- [ ] I stopped the session when the task breakdown was complete — I did not continue into implementation

## Task 3 — Handoff Prompt

- [ ] My handoff prompt contains Part 1 (summary of what the Planner produced)
- [ ] My handoff prompt contains Part 2 (the Implementer's bounded objective — one sub-task)
- [ ] My handoff prompt contains Part 3 (carry-forward: `.github/copilot-instructions.md` referenced)
- [ ] The handoff explicitly excludes other sub-tasks from the Implementer's scope

## Task 4 — All 10 Definitions

- [ ] All 10 definition files exist in `agents/`
- [ ] Security Reviewer has ❌ Edit, ✅ Web search, and a hallucination risk entry in Main Risks
- [ ] Solution Architect has ⚠️ Edit (docs only) — not ✅
- [ ] No two definitions claim contradictory ownership of the same role responsibility

---

## Mindset Check

- [ ] I understand why Reviewer roles never have ✅ Edit access
- [ ] I know the difference between ending a session cleanly and leaving it open
- [ ] I can state the 3-part handoff structure without referencing the module

---

## You're Ready for Module 07

All items above checked → proceed to [Module 07 — Multi-Agent Workflows](../../modules/07-multi-agent-workflows/).

Not all items checked → return to the task that produced the missing item, or revisit [Module 06 exercises](../../modules/06-agents/exercises.md).
