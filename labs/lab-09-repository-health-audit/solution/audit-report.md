# Lab 09: AI-Friendliness Audit — Reference Solution

## Score

| Property | Satisfied? | Finding |
|----------|:----------:|---------|
| Clear naming | ❌ | `utils.py`: single-letter functions (`fmt`, `h`, `check`, `clean`) provide no domain context. `api.py`: `do_stuff`, `handle`, `misc_check`, `update` describe no specific operation. `issues/task-1.md`: "Fix the stuff" provides no actionable scope. |
| Structured documentation | ❌ | `starter/README.md` has no labelled sections — prose only. No `## What this does`, `## Setup`, `## Project structure`. No function docstrings in any file. |
| Explicit conventions | ❌ | No `CONVENTIONS.md`. Two naming styles coexist: `get_user` (verb_noun) alongside `h`, `fmt`, `clean` (single-word abbreviations). No commit format documented. |
| Scoped context | ❌ | No `.copilotignore`. `API_KEY = "dev-key-12345"` is hardcoded in `api.py` — a Restricted-level value in plain source code. `DB_PATH` also hardcoded. |
| Minimal redundancy | ⚠️ Partial | No duplicate files visible. However, `utils.py` mixes date formatting, email validation, password hashing, ID generation, and logging — six distinct concern areas in one file. Mixed-concern files are a latent redundancy source as each concern grows independently. |
| Governed output | ❌ | No commit annotation standard documented. `issues/task-1.md` has no acceptance criteria. No review trail visible. |

**Score: 0/6 — High-noise environment. Fix before any large AI-assisted effort.**

---

## Ranked Remediation List

1. **Remove hardcoded `API_KEY` from `api.py`** — Restricted-level credential in source code. Move to an environment variable. Highest priority: credential in plaintext is a security failure independent of AI usage.

2. **Fix SQL injection in `get_user` and `update`** — OWASP A03 (Injection). F-string interpolation into SQL. Replace with parameterized queries immediately before any further development.

3. **Add `.copilotignore`** — Scoped context property. Exclude credential-adjacent files and generated output from AI context. Execute after items 1 and 2 so the entries reflect the corrected file inventory.

4. **Rename single-letter and filler functions in `utils.py` and `api.py`** — Clear naming property. `h` → `hash_password`, `fmt` → `format_date`, `check` → `validate_email`, `do_stuff` → `process_payment`, `handle` → `route_request`, `misc_check` → `is_non_empty`. Systematic renaming in one pass reduces import churn.

5. **Rewrite `README.md` with labelled sections** — Structured documentation property. The README is processed first in every session; fixing it amplifies the quality benefit of all other changes.

6. **Split `utils.py` by concern** — Clear naming property (completion). Suggested split: `date_utils.py`, `email_validators.py`, `password_utils.py`, `id_generator.py`. Defer until after function renaming to avoid double rename.

7. **Create `CONVENTIONS.md`** — Explicit conventions property. Prevents naming inconsistency from recurring after all fixes above are in place. Write after the codebase is cleaned, not before — conventions should describe what is, not what was.

8. **Rewrite `issues/task-1.md`** — Governed output property. Add: observed behavior, expected behavior, scope (files/functions), acceptance criteria.

> **Note on intentional problems in this lab:** The SQL injection vulnerabilities in `get_user` and `update` are deliberate learning artifacts. In a production codebase, items 1 and 2 would be patched as the highest priority before any other work proceeds.
