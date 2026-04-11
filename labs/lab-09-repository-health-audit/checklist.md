# Lab 09: Repository Health Audit — Completion Checklist

---

## Readiness

- [ ] I have completed the [Module 09 — AI-Friendly Repository Engineering](../../modules/09-repository-quality/) theory checklist.
- [ ] I can score a repository against the 6-property AI-friendliness checklist without referring to notes.
- [ ] I know all 5 gates of the pre-merge validation protocol.
- [ ] I know what distinguishes high-signal convention documentation from low-signal prose.

---

## Lab Completion

**Task 1 — AI-Friendliness Audit**

- [ ] I scored the starter repository against all 6 properties.
- [ ] My `audit-report.md` contains a score table and ranked finding list.
- [ ] I reviewed Copilot's assessment critically rather than accepting it verbatim.
- [ ] I compared my findings to `solution/audit-report.md`.

**Task 2 — README Restructure**

- [ ] I rewrote `starter/README.md` with all 6 required labelled sections.
- [ ] I did not invent content — missing information is acknowledged, not fabricated.
- [ ] The rewritten README passes the anti-pattern check from Module 09 theory.

**Task 3 — Governance Protocol**

- [ ] I applied all 5 gates of the pre-merge validation protocol to the provided diff.
- [ ] My `validation-report.md` records Pass/Fail/Partial per gate with a one-sentence finding.
- [ ] I identified Gate 4 (OWASP A03 — SQL Injection) as a BLOCKING failure.
- [ ] The overall result is correctly recorded as BLOCKED.

**Task 4 — `.copilotignore` Creation**

- [ ] My `.copilotignore` includes entries for all sensitive files identified in the audit.
- [ ] Every entry has an inline comment explaining why it is excluded.
- [ ] I can explain the difference between `.copilotignore` and `.gitignore` from memory.

**Task 5 — Convention Documentation**

- [ ] My `CONVENTIONS.md` uses the declarative, one-rule-per-bullet format.
- [ ] All 5 required sections are present (Naming, Imports, Tests, Commits, AI Context).
- [ ] The AI-assisted commit trailer format is documented.
- [ ] I compared my file to `solution/CONVENTIONS.md`.

---

## Lab Complete

All boxes above are checked.

→ Proceed to [Module 10 — Adoption Roadmap](../../modules/10-adoption-roadmap/) *(coming soon)*.
