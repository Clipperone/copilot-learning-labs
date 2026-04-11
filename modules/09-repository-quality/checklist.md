# Module 09: AI-Friendly Repository Engineering — Completion Checklist

Use the first section before Lab 09 as a readiness gate. Use the second section after Lab 09 to confirm completion.

---

## Before Lab 09 — Module Theory

**The 6-property AI-friendliness checklist**

- [ ] I can list all 6 properties of an AI-friendly repository from memory.
- [ ] I can explain the specific degradation that occurs when each property is missing.
- [ ] I know the scoring rule: what ≥ 5, 3–4, and ≤ 2 scores indicate.
- [ ] I can apply the checklist to a file tree and produce a ranked finding list.

**Documentation quality**

- [ ] I can list the required sections of an AI-useful README in the correct order.
- [ ] I understand why section order matters for AI context window loading.
- [ ] I can identify the anti-patterns: prose-first documentation, undifferentiated sections, buried conventions.
- [ ] I know the minimum content for each of the four inline documentation types (module, function, class, inline comment).
- [ ] I can write an issue description with all 4 required components.

**Naming and structure conventions**

- [ ] I can state the 4 naming principles from this module.
- [ ] I know the structure principle for small (≤ 20), medium (20–200), and large (200+) repositories.
- [ ] I know the minimum 5 items a `CONVENTIONS.md` must contain.
- [ ] I can distinguish between high-signal and low-signal convention documentation format.

**Governance of AI-generated code**

- [ ] I can describe the 3-tier audit trail (session log, diff annotation, merge annotation).
- [ ] I know which tiers are required for low, medium, and high risk commits.
- [ ] I can write a correctly formatted AI-assisted commit message with the `AI-assisted:` and `Reviewed-by:` trailers.
- [ ] I know when to omit the AI-assisted trailer.

**Pre-merge validation protocol**

- [ ] I can state all 5 gates of the pre-merge validation protocol.
- [ ] I know what condition causes each gate to fail.
- [ ] I know that a single gate failure blocks the merge.

**Repository size considerations**

- [ ] I know the appropriate convention set for small, medium, and large repositories.
- [ ] I can explain why over-engineering conventions for a small repo is as harmful as under-governing a large one.
- [ ] I know that convention sets must be versioned and updated as the repository grows.

---

## After Lab 09 — Lab Completion

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

- [ ] My `.copilotignore` includes all sensitive files identified in the audit.
- [ ] Every entry has an inline comment explaining why it is excluded.
- [ ] I can explain the difference between `.copilotignore` and `.gitignore` from memory.

**Task 5 — Convention Documentation**

- [ ] My `CONVENTIONS.md` uses the declarative, one-rule-per-bullet format.
- [ ] All 5 required sections are present (Naming, Imports, Tests, Commits, AI Context).
- [ ] The AI-assisted commit trailer format is documented.
- [ ] I compared my file to `solution/CONVENTIONS.md`.

---

## Module Complete

All boxes above are checked.

→ Advance to [Lab 09 — Repository Health Audit](../../labs/lab-09-repository-health-audit/) if not yet done.
→ Then proceed to [Module 10 — Adoption Roadmap](../../modules/10-adoption-roadmap/).
