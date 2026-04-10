# Pre-Commit Checklist

Use before every `git commit` on AI-assisted code. This checklist takes 2–5 minutes and prevents the most common AI-generated code problems from reaching the repository.

---

## Always (every commit)

- [ ] I have read every line of AI-generated code — not just the diff summary
- [ ] The code does what I asked, not just what it looks like it does
- [ ] All functions and methods are called correctly (no hallucinated APIs)
- [ ] Error cases are handled — the code is not happy-path only
- [ ] No credentials, tokens, API keys, or passwords are present in any file

---

## For Meaningful Changes (new functionality, refactors)

- [ ] Tests exist for the new behavior
- [ ] Existing tests still pass (`run test task` or `python -m pytest`)
- [ ] Linter shows no new errors or warnings (`ruff check .` or equivalent)
- [ ] Type annotations are present on new function signatures
- [ ] I understand the logic well enough to explain it to a colleague

---

## For Security-Sensitive Code

- [ ] User input is validated and sanitized before use
- [ ] No SQL or query string is built by string concatenation
- [ ] No third-party data is trusted without validation
- [ ] Authentication and authorization checks are present where required
- [ ] Relevant OWASP Top 10 categories have been considered:
  - [ ] A01: Broken Access Control
  - [ ] A02: Cryptographic Failures
  - [ ] A03: Injection
  - [ ] A07: Identification and Authentication Failures

---

## For Dependencies

- [ ] Any new `import` or `require` statement is intentional and necessary
- [ ] No abandoned or unmaintained packages were added
- [ ] Version constraints are specified, not open-ended (`>=`, not `*`)

---

## AI-Specific Risks

- [ ] Comments do not contain misleading explanations Copilot added incorrectly
- [ ] Copilot did not silently change behavior in unchanged-looking lines
- [ ] Generated test assertions test the real behavior, not a tautology (`assert result == result`)

---

## Reference

For a more detailed AI output review at any stage, see [checklists/ai-output-review.md](./ai-output-review.md).
