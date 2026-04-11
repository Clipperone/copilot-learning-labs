# Lab 09: Repository Health Audit

> **Difficulty:** Expert
> **Estimated time:** ~60 minutes
> **Module:** [Module 09 — AI-Friendly Repository Engineering](../../modules/09-repository-quality/)
> **Type:** Sequential — depends on [Lab 08 — Advanced Feature Tour](../lab-08-advanced-feature-tour/)

---

## Learning Objective

Audit a deliberately degraded Python repository against the 6-property AI-friendliness checklist, rewrite its documentation for AI-useful structure, apply the pre-merge validation protocol, and produce a machine-readable `CONVENTIONS.md`.

---

## Prerequisites

- [ ] Completed [Module 09 — AI-Friendly Repository Engineering](../../modules/09-repository-quality/) — module theory checklist fully checked
- [ ] GitHub Copilot Pro+ active in VS Code
- [ ] Python 3.10+ installed in the active environment
- [ ] Lab 08 complete

---

## Setup

1. Open this repository root in VS Code.
2. Open the terminal (`Ctrl+`` ` or `Cmd+`` `).
3. Navigate to the lab folder:

```bash
cd labs/lab-09-repository-health-audit
```

The `starter/` directory contains a small Python project with intentional structural problems. Do not fix the code problems before reading the task instructions — the problems are the learning material.

> ⚠️ **Security note:** The starter files contain deliberate vulnerabilities — including two SQL injection vectors — for learning purposes only. Do not use these files outside this lab exercise.

---

## Tasks

### Task 1 — AI-Friendliness Audit (15 min)

**Goal:** Score the `starter/` repository against the 6-property checklist and produce a prioritized issue list.

**Instructions:**

1. Open the `starter/` directory in VS Code. Review all files before opening Copilot.
2. Open Copilot Chat in Ask mode.
3. Describe the 6-property AI-friendliness checklist from Module 09 in your prompt. Ask Copilot to evaluate the starter files against each property.
4. Review Copilot's output critically — it may miss properties or mislabel findings. Apply your own judgment.
5. Produce a scoring table (0–6) and a ranked finding list with remediation priority.
6. Save your report as `starter/audit-report.md`.

**Expected output:** `starter/audit-report.md` with a score table, per-property findings, and a ranked remediation list.

> **Check against solution only after completing this task independently.** See `solution/audit-report.md`.

---

### Task 2 — README Restructure (15 min)

**Goal:** Rewrite `starter/README.md` using the AI-useful structure from Module 09.

**Instructions:**

1. Read the current `starter/README.md`. Note what information is present and what is missing.
2. Open Copilot Chat in Edit mode, scoped to `starter/README.md`.
3. Instruct Copilot to restructure the README using the 6-section AI-useful format:
   - `## What this does`
   - `## Setup`
   - `## Project structure`
   - `## Conventions`
   - `## Known limitations`
   - `## Architecture notes`
4. Review the output. Verify that:
   - All sections are present and labelled.
   - No content is invented — information not in the original file is marked as "Not yet documented."
   - Prose is contained in appropriate sections, not spread across the file.
5. Save the restructured file (overwrite `starter/README.md`).

**Expected output:** `starter/README.md` rewritten with all 6 required sections and no invented content.

**Failure points:**

- Copilot may invent setup steps not present in the original README. Reject and re-prompt: "Do not add information not present in the original file. Mark missing sections explicitly."
- Copilot may preserve narrative prose without adding section headings. Reject and specify: "Every content block must have a labelled heading."

---

### Task 3 — Governance Protocol (15 min)

**Goal:** Apply the pre-merge validation protocol to a staged diff and document the result.

**Instructions:**

1. Read `starter/api.py`. Identify the `get_user` function.
2. Treat the following as a proposed AI-generated replacement for `get_user`:

```python
def get_user(user_id: str) -> dict:
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = db.execute(query)
    return result[0] if result else {}
```

3. Apply all 5 gates of the pre-merge validation protocol from Module 09:
   - Gate 1: Scope
   - Gate 2: Ownership
   - Gate 3: Test coverage
   - Gate 4: OWASP check
   - Gate 5: Convention compliance
4. For each gate, record: Pass, Fail, or Partial — and a one-sentence finding.
5. State the overall result: APPROVED or BLOCKED, with the blocking gate(s) named.
6. Save your validation report as `starter/validation-report.md`.

**Expected output:** `starter/validation-report.md` with a 5-row gate table and an overall result.

> **Key finding:** Gate 4 (OWASP A03 — Injection) fails. The f-string interpolation creates a SQL injection vulnerability. The overall result must be BLOCKED.

---

### Task 4 — `.copilotignore` Creation (10 min)

**Goal:** Create a `.copilotignore` file that excludes noise and sensitive content from AI context.

**Instructions:**

1. Review all files in `starter/`. Identify:
   - Files containing sensitive information (credentials, keys, PII-adjacent logic)
   - Files that add noise without signal (generated files, large fixtures, vendored code)
2. Open Copilot Chat in Ask mode. Provide the file tree and ask: "Which of these files should be excluded from AI context and why?"
3. Review the suggestion. Add or remove entries based on your own judgment from Module 09 theory.
4. Create `starter/.copilotignore` with the entries you have identified.

**Expected output:** `starter/.copilotignore` with entries for sensitive or noise files, each with a brief inline comment.

**Success criteria:**

- At least one entry for a file containing sensitive information.
- At least one entry for a generated or cache directory.
- A comment per entry explaining why it is excluded.

---

### Task 5 — Convention Documentation (5 min)

**Goal:** Write a `CONVENTIONS.md` in machine-readable, declarative format.

**Instructions:**

1. Review `starter/api.py` and `starter/utils.py`. Note the naming style, import order, and any visible conventions — even if inconsistent.
2. Using the `CONVENTIONS.md` authoring guide from Module 09 theory as your reference, write a `CONVENTIONS.md` that:
   - Uses the high-signal, declarative format (one rule per bullet)
   - Contains sections for: Naming, Imports, Tests, Commits, AI Context
   - Documents the AI-assisted commit trailer format
3. Save as `starter/CONVENTIONS.md`.

**Expected output:** `starter/CONVENTIONS.md` in declarative format with all 5 sections.

> **Compare against `solution/CONVENTIONS.md` after completing this task.** The exact rules may differ; the format must match.

---

## Success Criteria

This lab is complete when:

1. `starter/audit-report.md` contains a 6-property score table and ranked finding list.
2. `starter/README.md` has been rewritten with all 6 required labelled sections.
3. `starter/validation-report.md` contains a 5-gate protocol result with BLOCKED outcome named.
4. `starter/.copilotignore` exists with entries for sensitive and noise files, each commented.
5. `starter/CONVENTIONS.md` exists in declarative format with 5 sections.

---

## Common Failure Points

| Failure | Cause | Recovery |
|---------|-------|----------|
| Copilot invents README content not in the original | No explicit "do not invent" constraint in the prompt | Re-prompt: "Use only information present in the original file. Mark missing sections with 'Not yet documented.'" |
| Gate 4 OWASP finding is missed | f-string SQL injection is easy to overlook | Explicitly prompt: "Check this function for SQL injection" if the initial review misses it |
| `.copilotignore` entries lack comments | Copilot generates uncommented entries by default | Ask Copilot to add an inline comment to each entry explaining the exclusion reason |
| `CONVENTIONS.md` output uses prose blocks | Copilot defaults to narrative when no format is specified | Provide the Module 09 declarative format explicitly as a constraint in the prompt |

---

## Extension Ideas

After completing all 5 tasks, these extensions apply the same skills to real-world contexts.

1. **Audit your own project** — Apply the 6-property checklist to an active repository you maintain. Produce a personal remediation plan ranked by impact; fix at least the top two items.
2. **Issue template** — Write a `.github/ISSUE_TEMPLATE/ai-assisted-task.md` that enforces the 4-component issue writing standard (observed behavior, expected behavior, scope, acceptance criteria).
3. **Session log template** — Create an `agents/session-log-template.md` that captures all Tier 1 audit-trail fields for any future AI session: date, task, prompt summary, model used, reviewer.
4. **Commit trailer CI check** — Configure a GitHub Actions workflow that blocks merge to `main` if the commit message body is missing both `AI-assisted:` and `Reviewed-by:` trailers on AI-assisted commits.
5. **Retrospective validation** — Pick a recent commit from your project history that was AI-assisted. Apply the 5-gate pre-merge protocol retroactively. Record which gates it passes and which it would have blocked.
