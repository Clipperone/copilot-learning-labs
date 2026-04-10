# AI Output Review Checklist

Apply this checklist to any AI-generated code before committing or merging.

> Use a lightweight scan (★☆☆) for low-risk changes like boilerplate. Use the full checklist (★★★) for business logic, security-sensitive code, and anything touching data, authentication, or external systems.

---

## Level 1 — Always Apply (every AI completion)

- [ ] The code compiles / runs without errors
- [ ] The code does what I asked — I read it line by line, not just scanned it
- [ ] Variable, function, and parameter names are accurate and match the codebase's naming conventions
- [ ] No obvious logic errors (off-by-one, wrong operator, inverted condition)
- [ ] No dead code or unnecessary scaffolding included

---

## Level 2 — Apply to Meaningful Code Changes

- [ ] Edge cases are handled: null/None, empty input, zero, negative values, empty collections
- [ ] Error handling is appropriate: exceptions caught where needed, not swallowed silently
- [ ] No hardcoded values where variables or config should be used
- [ ] Dependencies or imports introduced are intentional and available
- [ ] No deprecated APIs used — verified against current docs
- [ ] The code fits the existing architecture — it doesn't introduce a new pattern without reason
- [ ] If the function is async: concurrency is handled correctly (no race conditions, no blocking calls in async paths)

---

## Level 3 — Apply to Security-Sensitive and Production Code

- [ ] No user input passed directly to SQL queries, shell commands, file paths, or eval (injection risk)
- [ ] No secrets, credentials, API keys, or tokens present — even in comments or test data
- [ ] Authentication and authorization checks are not bypassed or incomplete
- [ ] Sensitive data is not logged, written to disk unencrypted, or leaked in error messages
- [ ] No use of `eval()`, `exec()`, `pickle.loads()`, or similar unsafe deserialization
- [ ] Cryptographic operations use current recommended algorithms (not MD5, SHA1, DES)
- [ ] File operations validate paths to prevent directory traversal
- [ ] Any network request validates TLS and does not disable certificate verification
- [ ] OWASP Top 10 implications considered for this code path

---

## Level 4 — Apply Before Committing

- [ ] Tests cover the new or changed code (or I've documented why tests are deferred)
- [ ] Existing tests still pass after the change
- [ ] Documentation is updated if a public API or behavior changed
- [ ] The commit message describes what changed and why — not just "AI-generated"
- [ ] The change is isolated — no unrelated modifications included

---

## Notes

- For rapid review, ask Copilot: `Review this code for correctness, edge cases, and security issues. Be specific.`
- For security review, use the agent definition at [agents/security-reviewer.md](../agents/security-reviewer.md) *(available in v0.4)*.
- For the full pre-commit workflow, see [checklists/pre-commit.md](./pre-commit.md) *(available in v0.2)*.
