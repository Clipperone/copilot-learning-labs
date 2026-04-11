# Lab 08: Advanced Feature Tour — Completion Checklist

---

## Pre-Lab Readiness

- [ ] Module 08 theory checklist fully checked
- [ ] Lab 07 complete — at least one multi-agent workflow was run end-to-end
- [ ] VS Code terminal is open and `pytest` responds to `pytest --version`
- [ ] A Code Reviewer persona definition exists in `agents/code-reviewer.md` (created in Lab 06)

---

## Task 1 — Plan Before You Code

- [ ] I used Plan mode (not Edit or Agent) for the design step
- [ ] My Plan output names exactly which files to modify and why
- [ ] My Plan output states what will NOT change
- [ ] My Plan output contains a problem restatement in the AI's own words
- [ ] My Plan output contains at least one open question or a statement that no ambiguity remains
- [ ] I did not write any implementation code during Task 1
- [ ] `starter/plan-output.md` is committed

---

## Task 2 — AI-Assisted Code Review

- [ ] I opened a Code Reviewer Agent session scoped to `starter/api/routes.py` only
- [ ] I used the initialization prompt structure from the task instructions
- [ ] I produced a numbered findings document
- [ ] Every finding has: number, severity, file and line, description, and suggested fix
- [ ] I have at least one High or Medium finding
- [ ] `starter/review-findings.md` is committed

---

## Task 3 — Terminal Integration

- [ ] I ran the failing pytest command and observed the `ModuleNotFoundError`
- [ ] I used `@terminal` to explain the error
- [ ] I used `@terminal` to request a corrected command
- [ ] I applied the 4-question gate to the suggested command before running it
- [ ] The corrected command ran without import errors

---

## Task 4 — Quality Gate

- [ ] I ran `PYTHONPATH=starter pytest starter/tests/ -v` (or equivalent)
- [ ] The output shows `3 passed` with exit code 0
- [ ] Zero failures, zero errors

---

## Task 5 — Secure Usage

- [ ] I classified all 3 starter files using the 4-level framework
- [ ] I identified all 3 OWASP issues in `auth.py` (MD5 hashing, hardcoded salt, missing input validation)
- [ ] I wrote at least one `.copilotignore` entry based on my classification
- [ ] `starter/sensitivity-classification.md` is committed
- [ ] I compared my findings to `solution/secure-usage-checklist.md`

---

## Lab Complete

All boxes above are checked.

→ Return to [Module 08 checklist](../../modules/08-advanced-features/checklist.md) and check the "After Lab 08" section.
→ Then advance to [Module 09 — Repository Quality for AI](../../modules/09-repository-quality/) *(coming soon)*.
