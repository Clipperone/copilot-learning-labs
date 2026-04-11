# CONVENTIONS.md

Verified: 2026-04

---

## Naming

- Files: `snake_case.py` — one concern per file; name describes the concern (`payment_processor.py`, not `utils.py`)
- Functions: `verb_noun()` format — `get_user()`, `validate_email()`, `format_date()`
- No abbreviations or single-letter names (except loop variables `i`, `j`, `k`)
- No filler names: `helpers`, `utils`, `misc`, `handle`, `do_stuff`, `manager` are not acceptable standalone file or function names
- Constants: `UPPER_SNAKE_CASE`
- Classes: `PascalCase`

## Imports

- Standard library first
- Third-party second
- Local last
- One blank line between groups
- No wildcard imports (`from module import *`)

## Tests

- Test files: `test_<module_name>.py` in `tests/` directory
- Test functions: `test_<function_name>_<scenario>()`
- No shared mutable state between tests
- Each test covers one path (happy path or one failure mode)
- No real credentials or PII in test data

## Commits

- Format: Conventional Commits (`feat`, `fix`, `refactor`, `docs`, `test`, `chore`)
- Imperative description: "add password reset endpoint" not "added password reset endpoint"
- Body explains why, not what
- AI-assisted commits include `AI-assisted:` trailer with a brief review note
- All non-trivial AI-assisted commits require a `Reviewed-by:` trailer

Example:

```
fix(auth): use parameterized queries in get_user

AI-assisted: suggested parameterized query replacement; reviewed against OWASP A03.
Reviewed-by: [name]
```

## AI Context

- `.copilotignore` controls context exclusion — see file for current entries
- Default session scope: one directory; state scope explicitly in the first prompt
- Hardcoded credentials are Restricted — must not appear in any AI context
- Sensitive files: apply sensitivity classification from Module 08 before each session
- Pre-merge validation: apply all 5 gates before committing any AI-assisted function
