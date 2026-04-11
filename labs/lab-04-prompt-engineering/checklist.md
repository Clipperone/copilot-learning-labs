# Lab 04 — Completion Checklist

Use this checklist after completing all four tasks. Each item maps to a specific task in [README.md](./README.md).

---

## Task 1 — First Four Scenarios

- [ ] I wrote a generation prompt that added type annotations, validation, and a return type to `parse_config`.
- [ ] I wrote a refactoring prompt that extracted `_get_tax_rate` from `calculate_tax` without changing the public interface.
- [ ] I used a two-prompt chain for `merge_sorted`: diagnosis first, fix second.
- [ ] My debugging chain confirmed the root cause before I accepted the fix.
- [ ] I wrote a testing prompt that produced four named test functions covering valid code, invalid code, zero price, and negative price.

## Task 2 — Last Three Scenarios

- [ ] I wrote a documentation prompt that produced a Google-style docstring with `Args`, `Returns`, and `Raises`.
- [ ] I wrote two separate review prompts for `check_permissions` — one scoped to logic errors, one to OWASP A01.
- [ ] I used a premium model (o1 or Claude) for the `hash_password` security review.
- [ ] My security review prompt cited OWASP A02:2021 explicitly.
- [ ] I wrote the OWASP risk name in a comment before accepting the fix.
- [ ] `hash_password` no longer uses MD5.

## Task 3 — Anti-pattern Diagnosis

- [ ] I named the anti-pattern in Prompt A: double task (fix + test in one prompt).
- [ ] I named the anti-pattern in Prompt B: premature fix (no context, no OWASP scope).
- [ ] I named the anti-pattern in Prompt C: context dump (too broad, no specific question).
- [ ] I rewrote all three prompts using the 4-component structure.

## Task 4 — Prompt Library

- [ ] `prompts/testing/write-tests.md` exists with all fields complete.
- [ ] `prompts/documentation/write-docstring.md` exists with all fields complete.
- [ ] `prompts/review/code-review.md` exists with all fields complete.
- [ ] `prompts/security/security-audit.md` exists with all fields complete.
- [ ] `prompts/migration/migrate-api.md` exists with all fields complete.
- [ ] No file contains a `[PLACEHOLDER]` stub — all fields are filled in.
- [ ] Each file has at least one row in its "Common Failures" table.

## Success Criteria Verification

- [ ] `parse_config("nonexistent.toml")` raises `FileNotFoundError` with a descriptive message.
- [ ] `merge_sorted([1,3], [2])` returns `[1, 2, 3]`.
- [ ] Running `pytest` on the test file produces 4 passing tests.
- [ ] `validate_email` has a Google-style docstring in the function body.
- [ ] `hash_password` uses `pbkdf2_hmac` or `bcrypt` — not `md5`.

---

## All items checked?

→ Proceed to [Module 05 — Persistent Custom Instructions](../../modules/05-custom-instructions/)

## Items not checked?

Return to [README.md](./README.md) for the specific task, or check [solution/workbench.py](./solution/workbench.py) for the reference implementation.
