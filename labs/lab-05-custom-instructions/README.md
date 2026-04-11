# Lab 05 — Write Your Project's Custom Instructions

> **Paired module:** [Module 05 — Persistent Custom Instructions](../../modules/05-custom-instructions/)
> **Level:** Intermediate
> **Estimated time:** ~50 minutes
> **Prerequisites:** Module 05 complete · Lab 04 complete

---

## Objective

Write all three tiers of custom instructions for a sample Python project — global, repository-wide, and path-specific — and verify that each instruction is applied automatically by Copilot without restating it in a prompt.

By the end of this lab you will have:

- Classified project constraints by the correct instruction scope.
- A working `.github/copilot-instructions.md` that encodes architecture, testing, security, and documentation rules.
- A path-specific instruction file for the API layer using `applyTo` frontmatter.
- Verified evidence that Copilot applies instructions without prompt repetition.

---

## Prerequisites

- [ ] Completed [Module 05 — Persistent Custom Instructions](../../modules/05-custom-instructions/)
- [ ] Completed [Lab 04 — Prompt Engineering Workshop](../lab-04-prompt-engineering/)
- [ ] GitHub Copilot Pro+ active in VS Code
- [ ] VS Code with the GitHub Copilot Chat extension installed

---

## Setup

1. Open this repository root in VS Code.
2. Navigate to `labs/lab-05-custom-instructions/starter/` — this is the project you will write instructions for.
3. Open the Copilot Chat panel (`Ctrl+Alt+I` / `Cmd+Alt+I`).
4. Keep [Module 05 README.md](../../modules/05-custom-instructions/README.md) open as a reference tab.
5. Do not open the `solution/` folder before completing Task 3.

---

## Tasks

### Task 1 — Scope Analysis (10 min)

**Goal:** Classify each constraint by the correct instruction scope before writing a single line.

Read through the starter project files in `starter/`. Then classify each constraint in the table below.

| # | Constraint | Your scope assignment: global / repo-wide / path-specific |
|---|-----------|-----------------------------------------------------------|
| 1 | "All public functions must have Google-style docstrings." | |
| 2 | "Do not use MD5 or SHA1 for password hashing." | |
| 3 | "Do not return raw dicts from route handlers — use a typed model." | |
| 4 | "I always prefer snake_case for identifiers." | |
| 5 | "Use pytest. One test function per case." | |
| 6 | "Validate all request input at the route handler boundary." | |

**Expected output:**

A completed table with each constraint assigned to one of: global, repo-wide, or path-specific — with reasoning you can state aloud.

Reference answers are in [solution/README.md](./solution/README.md). Do not open it until you have completed your own classification.

---

### Task 2 — Write the Repository-Wide Instruction File (15 min)

**Goal:** Author `.github/copilot-instructions.md` in the starter project to encode project-level constraints.

**Instructions:**

1. Create the file `labs/lab-05-custom-instructions/starter/.github/copilot-instructions.md`.
2. Add a Verified comment block at the very top:
   ```markdown
   <!--
     Verified: YYYY-MM
     Update this date whenever you make a material change.
   -->
   ```
3. Write instruction statements covering at least four of the five domains:
   - **Coding style:** snake_case identifiers, type annotations on all parameters and return values, max line length 100.
   - **Architecture:** no direct data access from route handlers; all data access through the model layer.
   - **Testing:** pytest, one test function per case, bare assert statements, cover null/empty/boundary cases.
   - **Security:** no MD5 or SHA1 for hashing; flag OWASP A02 and A03 risks in auth or data-processing code.
   - **Documentation:** Google-style docstrings with Args, Returns, and Raises on every public function.
4. Apply the 4 design principles to every statement: specific, imperative, bounded, non-contradictory.
5. Keep total prose under 400 words.

**Expected output:**

A `.github/copilot-instructions.md` file with clearly separated domain sections, each containing at least one quantified instruction statement. The file is under 400 words of prose.

---

### Task 3 — Write a Path-Specific Instruction File (10 min)

**Goal:** Author an instruction file for the API layer that tightens the contract beyond the repo-wide rules.

**Instructions:**

1. Create `labs/lab-05-custom-instructions/starter/.github/instructions/api-layer.instructions.md`.
2. At the very start of the file, add `applyTo` frontmatter:
   ```markdown
   ---
   applyTo: "src/api/**"
   ---
   ```
3. Write instruction statements that add API-layer specificity — do not repeat anything already in the repo-wide file:
   - All route handlers must validate request input at the boundary before passing to the model layer.
   - All route handlers must return a typed model (TypedDict or dataclass) — never a raw dict.
   - Flag OWASP A03:2021 (Injection) on any query or command construction.
   - Return structured error responses. Never expose stack traces or internal messages in HTTP responses.
4. Keep prose under 200 words.

**Expected output:**

A `.instructions.md` file whose first content is the `---` frontmatter block, containing `applyTo: "src/api/**"`. Constraints do not duplicate the repo-wide file — they add a stricter contract for the API layer.

---

### Task 4 — Verify Instructions Are Active (10 min)

**Goal:** Confirm that Copilot reads and applies both instruction files automatically.

**Instructions:**

1. Open the Copilot Chat panel and select **Ask** mode.
2. Run this diagnostic prompt exactly:

   ```
   Task: Add a new route handler `get_user_profile(user_id)` to `src/api/users.py`.
   Output: The function only.
   ```

3. Check the output against your instruction files using this checklist:
   - [ ] Type annotations present on parameters and return value? (coding style)
   - [ ] Google-style docstring included? (documentation)
   - [ ] Return is a typed model, not a raw dict? (API-specific)
   - [ ] Input is validated before use? (API-specific)
4. If an expected rule is absent, diagnose using the 3-sign checklist from Module 05:
   - Is the file at the exact required path?
   - Does the file exceed ~400 words of prose?
   - Are any statements passive ("it is preferred that...") rather than imperative?
5. Fix any problems found and re-run the diagnostic until at least four rules appear without being prompted.

**Expected output:**

A Copilot response that applies at least four instruction rules automatically, confirmed by the checklist above.

---

## Expected Outputs

By the end of this lab, you will have produced:

- [ ] A scope-assignment table with all six constraints correctly classified (Task 1)
- [ ] `starter/.github/copilot-instructions.md` — five domains, ≤400 words prose, Verified comment dated (Task 2)
- [ ] `starter/.github/instructions/api-layer.instructions.md` — `applyTo` frontmatter, API-specific constraints only (Task 3)
- [ ] Verification evidence: at least four rules applied in diagnostic output without prompting (Task 4)

---

## Success Criteria

| Criterion | How to verify |
|-----------|---------------|
| Repo-wide instruction file is active | File exists at `starter/.github/copilot-instructions.md`. Diagnostic output shows at least one coding-style and one documentation rule applied automatically. |
| Path-specific file is active | File exists at `starter/.github/instructions/api-layer.instructions.md` with `applyTo: "src/api/**"` frontmatter. API-specific rules appear in diagnostic output without being stated in the prompt. |
| No cross-file duplication | Open both files. Every statement appears in exactly one file. The path-specific file adds constraints — it does not restate repo-wide constraints. |
| 4-principle compliance | Read each instruction aloud. It must: name what to produce (specific), use an imperative verb (imperative), state a limit (bounded), and not contradict another in-scope instruction (non-contradictory). |
| Verified comment present | Both instruction files begin with the Verified comment block. |

---

## Common Failure Points

| Symptom | Likely cause | Solution |
|---------|-------------|---------|
| Diagnostic output ignores instruction rules entirely | Wrong file path — `.github/copilot-instructions.md` is case-sensitive and must be in `.github/`, not `github/` or `.Github/` | Verify the path character by character; rename if needed |
| Path-specific file has no effect | Missing or malformed `applyTo` frontmatter | The `---` delimiter must be on its own line, appear as the very first content in the file, and close with another `---` line |
| API rule missing but repo-wide rules apply | Path-specific file loaded but diagnostic prompt was not run against a file matching the glob | Open `src/api/users.py` in the editor, then run the diagnostic with that file as active context |
| Instruction file too long | Writing too many rules in a single file | Keep prose under 400 words; split by domain if needed — Copilot silently truncates what does not fit in context |
| Contradiction between global and repo-wide | Personal naming convention in global setting conflicts with repo convention | Remove the global rule when the repo has a convention; repo-wide wins in a project context |

---

## Review Checklist

See [checklist.md](./checklist.md) for the full self-assessment checklist.

---

## Extension Ideas

1. **Global instruction file:** Write a global instruction fragment for your personal habits using the VS Code `github.copilot.chat.codeGeneration.instructions` setting. Compare output before and after adding it to the repo-wide file.

2. **Security hardening:** `starter/src/api/auth.py` uses MD5 for password hashing — an OWASP A02:2021 violation. Write a security instruction that flags this pattern, then run a Copilot security review on `auth.py`. Confirm Copilot flags the MD5 usage automatically.

3. **Deliberate contradiction test:** Introduce a contradictory rule between the repo-wide and path-specific files. Run the diagnostic and observe which rule wins. Record the result in a comment.

4. **Team portability exercise:** Review your instruction file and identify which constraints are project-specific versus machine-specific versus purely personal preference. Refactor into the correct scope for each.
