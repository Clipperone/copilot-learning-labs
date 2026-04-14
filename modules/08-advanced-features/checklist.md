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

**Plan → Implementer handoff (Exercise 6)**

- [ ] I completed Exercise 6 — converted a 5-element Plan output into a bounded Implementer initialization prompt.
- [ ] My initialization prompt names the file allowlist, exit condition, and explicit exclusions.
- [ ] I wrote a 3-item verification checklist, each item tied to a specific element of the plan.
- [ ] I correctly diagnosed plan drift in the scenario and chose reject-or-replan over silent acceptance.

**Edits-style workflows in Agent mode (Exercise 7)**

- [ ] I know that Edit mode was consolidated into Agent mode in VS Code 1.110 and can describe how to do "edits-style" multi-file coordinated changes in Agent mode today.
- [ ] I can scope an Agent session to act like the old Edits flow (explicit `#file:` set, no terminal, per-file review).
- [ ] I can choose between Agent (default), a custom agent (reusable scoped persona), and inline chat (single-file local edit).
- [ ] I completed Exercise 7 — coordinated rename across 3 files in Agent mode with discipline rules enforced; the test still passed.

**Model Context Protocol (Exercise 8)**

- [ ] I can explain in one sentence what MCP is and why it is the durable extensibility surface for Copilot.
- [ ] I configured one MCP server (`@modelcontextprotocol/server-filesystem`) at `.vscode/mcp.json` scoped to a sub-directory, not repo root.
- [ ] I can name the 4 fields of an MCP tool call from a trace: server, tool, arguments, result.
- [ ] I verified the scope boundary by attempting an out-of-scope read and confirming the server refused.
- [ ] I can choose between MCP, a custom agent, an instruction file, and a prompt file given a need.

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
→ Then proceed to [Module 09 — AI-Friendly Repository Engineering](../../modules/09-repository-quality/).
