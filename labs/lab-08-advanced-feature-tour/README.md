# Lab 08: Advanced Feature Tour

> **Difficulty:** Expert
> **Estimated time:** ~60 minutes
> **Module:** [Module 08 — Advanced Features](../../modules/08-advanced-features/)
> **Type:** Sequential — depends on [Lab 07 — Run a Complete Multi-Agent Workflow](../lab-07-multi-agent-workflow/)

---

## Learning Objective

Apply Plan mode, AI-assisted code review, terminal integration, quality gate tooling, and secure usage classification in five consecutive tasks against the same codebase.

---

## Prerequisites

- [ ] Completed [Module 08 — Advanced Features](../../modules/08-advanced-features/) — module theory checklist fully checked
- [ ] GitHub Copilot Pro+ active in VS Code
- [ ] Python 3.10+ and `pytest` installed in the active environment
- [ ] Lab 07 complete — at least one multi-agent workflow run end-to-end

---

## Setup

1. Open this repository root in VS Code.
2. Open the terminal (`Ctrl+`` ` or `Cmd+`` `).
3. Navigate to the lab folder:

```bash
cd labs/lab-08-advanced-feature-tour
```

4. Confirm pytest is available:

```bash
pytest --version
```

> **Output file locations:** Tasks 1, 2, and 5 ask you to save output files inside `starter/`. This is intentional — all lab tasks operate against the same starter codebase and outputs live alongside the files that generated them.

---

## Tasks

### Task 1 — Plan Before You Code (15 min)

**Goal:** Use Plan mode to design `delete_item()` before writing any code.

**Feature specification:**

> Add a `delete_item(item_id: str, requesting_user_id: str) -> None` function to `api/routes.py`. Only the owner of an item may delete it. Deleting a non-existent item raises `ValueError`. Deleting an item the requesting user does not own raises `PermissionError`. All deletions must be audited before the item is removed.

**Instructions:**

1. Open `starter/api/routes.py` in the editor. Review the existing functions and the `TODO` comment at the bottom.
2. Switch Copilot Chat to **Plan mode**.
3. Describe the feature specification above as your prompt. Do not paste code — describe the requirement only.
4. When Plan mode returns a response, evaluate it against the 5-element checklist:
   - One-paragraph problem restatement in the AI's own words
   - Files to modify with one sentence of reasoning per file
   - Proposed change per file at function scope (not line-by-line code)
   - Explicit statement of what will NOT change
   - One open question if any scope ambiguity exists
5. If any element is missing, add a constraint to your prompt and re-run Plan mode.
6. Once the output passes the checklist, copy it to `starter/plan-output.md` and commit.

**Expected output:** `starter/plan-output.md` committed, Plan mode output passes all 5 checklist elements.

> **Check against solution only after completing this task independently.** See `solution/plan-output.md`.

---

### Task 2 — AI-Assisted Code Review (15 min)

**Goal:** Run a Code Reviewer Agent session on `api/routes.py` and produce a numbered findings document.

**Instructions:**

1. Switch Copilot Chat to **Agent mode**.
2. Open a Code Reviewer session using the Code Reviewer persona definition from `agents/code-reviewer.md` (created in Lab 06). Scope the session to `starter/api/routes.py` only.

   > **Prerequisite check:** This task requires `agents/code-reviewer.md` to be complete and passing the completeness test. If this file is absent or contains `[PLACEHOLDER]` stubs, return to [Lab 06 Task 1](../lab-06-agents-and-personas/) before continuing.
3. Use this initialization prompt:

   ```
   Role: Act as a Code Reviewer.
   Purpose: Review starter/api/routes.py for correctness, missing validation, and style issues.
   Scope: starter/api/routes.py only. Do not review auth.py or test files.
   Constraints:
   - Do not edit any file.
   - Produce numbered findings only.
   - Each finding must include: number, severity (Critical/High/Medium/Low), file and line, description, and suggested fix.
   Exit condition: All findings documented; no further questions.
   ```

4. When the session produces findings, close the session.
5. Save the findings as `starter/review-findings.md` and commit.

**Expected output:** `starter/review-findings.md` committed; at least 2 findings; every finding has severity, location, and suggested fix.

> **Check against solution only after completing this task independently.** See `solution/review-findings.md`.

---

### Task 3 — Terminal Integration (10 min)

**Goal:** Use `@terminal` to explain a pytest import error and validate the corrected command before running it.

**Instructions:**

1. In the terminal (from `labs/lab-08-advanced-feature-tour/`), run:

   ```bash
   pytest starter/tests/test_routes.py
   ```

2. You will see a `ModuleNotFoundError: No module named 'api'`.
3. In the VS Code terminal, type:

   ```
   @terminal explain this error: ModuleNotFoundError: No module named 'api'
   ```

4. Review the explanation. Ask for a corrected command:

   ```
   @terminal give me the corrected pytest command to run starter/tests/test_routes.py from this directory
   ```

5. Before running the suggested command, apply the 4-question gate:
   - Does it do what I asked?
   - Does it do anything I did not ask?
   - Is it reversible?
   - Am I confident enough to own the outcome?

6. Run the corrected command only after passing all four gates.

**Expected output:** Corrected pytest command runs without the import error; all tests collected successfully.

---

### Task 4 — Quality Gate with pytest (10 min)

**Goal:** Run the full test suite with the corrected command and confirm zero failures and zero errors.

**Instructions:**

1. Build on the corrected command from Task 3.
2. Run the corrected pytest command from Task 3 with verbose output:

   ```bash
   PYTHONPATH=starter pytest starter/tests/ -v
   ```

   *(On Windows without a Unix shell, use `$env:PYTHONPATH="starter"; pytest starter/tests/ -v` in PowerShell.)*

2. Review the output. All 3 tests should pass.
3. If any test fails, paste the failure into Copilot Ask mode and ask for an explanation.
4. Confirm: zero failures, zero errors before moving to Task 5.

**Expected output:** `pytest` exits with code 0; all 3 tests pass; output shows `3 passed`.

---

### Task 5 — Secure Usage Classification (10 min)

**Goal:** Classify the starter files by sensitivity level, write `.copilotignore` entries, and identify OWASP issues in `auth.py`.

**Instructions:**

1. Open each file in `starter/` and classify it using the 4-level framework from Module 08:

   | Level | Definition |
   |-------|-----------|
   | Public | No sensitive data; no restriction |
   | Internal | Business logic; permitted in session; exclude from prompt examples |
   | Confidential | Security-adjacent; session allowed; never paste verbatim; findings not shared externally without redaction |
   | Restricted | Credentials or secrets; never in any AI context |

2. For any file you classify as Restricted, write a `.copilotignore` entry for it.

3. Open a new Copilot Ask mode chat and ask:

   ```
   Review starter/auth.py for OWASP Top 10 issues. For each issue, state: the OWASP category, the specific function and line, and the minimum fix.
   ```

4. Record your classification and OWASP findings in `starter/sensitivity-classification.md`.
5. Commit the file.

**Expected output:** `starter/sensitivity-classification.md` committed; classification table covers all 3 starter files; 3 OWASP issues in `auth.py` identified.

> **Check against solution only after completing this task independently.** See `solution/sensitivity-classification.md`.

---

## Expected Outputs

By the end of this lab, you should have produced:

- [ ] `starter/plan-output.md` — Plan mode output for `delete_item()`, all 5 elements present
- [ ] `starter/review-findings.md` — numbered Code Review findings for `api/routes.py`
- [ ] Corrected pytest command verified and executed (Task 3)
- [ ] `pytest` exit code 0 — all 3 tests pass (Task 4)
- [ ] `starter/sensitivity-classification.md` — classification table + OWASP findings + `.copilotignore` entries

---

## Success Criteria

| Criterion | How to verify |
|-----------|---------------|
| Plan output has all 5 elements | Open `starter/plan-output.md`; check each element against the checklist |
| Each review finding is actionable | Open `starter/review-findings.md`; confirm severity + file/line + suggested fix present on every finding |
| Corrected pytest command used | Terminal shows `PYTHONPATH=starter pytest` or equivalent — no import errors |
| All tests pass | Terminal shows `3 passed` with exit code 0 |
| Sensitivity classification complete | `starter/sensitivity-classification.md` has a row for each starter file |
| OWASP issues documented | Classification file names all 3 issues in `auth.py`: MD5 hashing, hardcoded salt, no input validation |
| `.copilotignore` entries present | At least one entry covering any Restricted files identified |

---

## Common Failure Points

| Symptom | Likely cause | Solution |
|---------|-------------|---------|
| Plan mode output has no "what will NOT change" section | Plan mode was not prompted with sufficient constraints | Restate: "Include an explicit section listing what will NOT change" |
| Code Reviewer session produces vague findings | No explicit finding format required in the init prompt | Add: "Each finding must include: number, severity, file, line, description, suggested fix" |
| `ModuleNotFoundError` persists after correction | PYTHONPATH not set correctly or wrong working directory | Confirm you are in `labs/lab-08-advanced-feature-tour/` and `PYTHONPATH=starter` points to the `starter/` subfolder |
| Task 5 classification marks everything as Confidential | Over-broad classification | Apply the 4-level definition strictly; README and test files with no real data are Internal or Public |
| `auth.py` OWASP query returns only 1 issue | Model did not scan the full file | Re-ask with explicit scope: "Review all functions in auth.py, not just hash_password()" |

---

## Review Checklist

See [checklist.md](./checklist.md) for the full self-assessment checklist.

---

## Extension Ideas

- Implement `delete_item()` using the Plan mode output from Task 1 in an Implementer Agent session (Lab 07 pattern).
- Add tests for the ownership check and `ValueError` paths in a Test Engineer session.
- Run `ruff check --select S starter/auth.py` and compare the tool output to your Task 5 OWASP findings.
- Add a Security Reviewer Agent session on `auth.py` with an explicit OWASP exploit-path requirement.

---

## Files in This Lab

| File / Folder | Purpose |
|---------------|---------|
| `README.md` | Lab instructions (this file) |
| `checklist.md` | Completion checklist |
| `starter/` | Starter files — begin here |
| `starter/auth.py` | Authentication helpers with intentional OWASP issues (Task 5) |
| `starter/api/routes.py` | API route stubs with `delete_item()` TODO (Tasks 1–2) |
| `starter/tests/test_routes.py` | Partial test coverage — GET only (Tasks 3–4) |
| `solution/plan-output.md` | Reference Plan mode output |
| `solution/review-findings.md` | Reference Code Reviewer findings |
| `solution/sensitivity-classification.md` | Reference sensitivity classification and OWASP findings |
