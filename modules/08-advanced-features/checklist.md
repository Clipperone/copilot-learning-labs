# Module 08: Advanced Features in Copilot + VS Code — Completion Checklist

Use the first section before Lab 08 as a readiness gate. Use the second section after Lab 08 to confirm completion.

---

## Before Lab 08 — Module Theory

**Plan mode**

- [ ] I can state the 5 elements a complete Plan mode output must contain.
- [ ] I can explain why Plan mode output is a proposal, not code.
- [ ] I can state when Plan mode is preferable over an Agent Planner session.
- [ ] I know at least two signals that indicate a Plan mode output is incomplete or incorrect.

**AI-assisted code review**

- [ ] I can describe the 5-step structured review loop.
- [ ] I can distinguish an actionable finding from a non-actionable one.
- [ ] I know what AI review catches well and what it does not replace.
- [ ] I know when to escalate a Code Reviewer session to a premium model.

**Terminal and CLI integration**

- [ ] I can use `@terminal` to explain a shell error.
- [ ] I can apply the 4-question gate to any AI-generated command before executing it.
- [ ] I can name two command types that always require explicit caution (`git reset --hard`, `git push --force`).

**Quality tool integration**

- [ ] I can state the 4 components of the minimum quality gate before commit.
- [ ] I know how to use Copilot to interpret a pytest failure in the terminal.
- [ ] I understand that Copilot suggestions in CI pipelines require the same human review gate as inline completions.

**Large repository context management**

- [ ] I know at least 3 techniques for scoping context in a large repository.
- [ ] I can write a `.copilotignore` file for a given file inventory.
- [ ] I can state the sizing rule for session file scope (maximum files not in the init prompt).

**Secure usage patterns**

- [ ] I can classify any file as Public, Internal, Confidential, or Restricted.
- [ ] I know the 4 credential hygiene rules from this module.
- [ ] I can apply the 5-category OWASP minimum check to any AI-generated function.
- [ ] I know when a `.copilotignore` entry alone is insufficient for compliance requirements.

---

## After Lab 08 — Lab Completion

**Task 1 — Plan Before You Code**

- [ ] I used Plan mode (not Edit or Agent) for the design step.
- [ ] My Plan output contains all 5 required elements.
- [ ] I saved the output as `starter/plan-output.md` and compared it to `solution/plan-output.md`.
- [ ] I did not write any implementation code during Task 1.

**Task 2 — AI-Assisted Code Review**

- [ ] I ran a Code Reviewer Agent session on `api/routes.py`.
- [ ] I produced a numbered findings document saved as `starter/review-findings.md`.
- [ ] Every finding has: number, severity, file and line, description, and suggested fix.
- [ ] I compared my findings to `solution/review-findings.md`.

**Task 3 — Terminal Integration**

- [ ] I ran the failing pytest command and observed the import error.
- [ ] I used `@terminal` to explain the error.
- [ ] I applied the 4-question gate to the AI-suggested correction before running it.
- [ ] The corrected command ran without import errors.

**Task 4 — Quality Gate**

- [ ] All 3 starter tests pass with zero failures and zero errors.
- [ ] I used Copilot in Ask mode to interpret at least one test output line.

**Task 5 — Secure Usage**

- [ ] I classified all 3 starter files by sensitivity level.
- [ ] I identified all 3 OWASP issues in `auth.py`.
- [ ] I saved my classification as `starter/sensitivity-classification.md`.
- [ ] I compared my classification and OWASP findings to `solution/sensitivity-classification.md`.

---

## Module Complete

All boxes above are checked.

→ Advance to [Lab 08 — Advanced Feature Tour](../../labs/lab-08-advanced-feature-tour/) if not yet done.
→ Then proceed to [Module 09 — Repository Quality for AI](../../modules/09-repository-quality/) *(coming soon)*.
