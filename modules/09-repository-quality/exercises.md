# Module 09: AI-Friendly Repository Engineering — Exercises

Complete these exercises in order. Expected answers are provided after each exercise — work through the problem independently before reading the answer.

---

## Exercise 1 — AI-Friendliness Score

**Type:** Evaluation
**Time:** ~15 minutes

**Context:**

A development team uses the following directory structure and documentation setup:

```
project/
├── README.md         # 200-word prose "About" section; no headings beyond H1
├── helpers.py        # 18 functions: validation, formatting, date math, email parsing
├── main.py
├── models.py
├── api.py            # 500 lines: routes, serialization, auth middleware, error handling
├── tests/
│   └── test_main.py  # 6 tests, all for main.py
└── .env              # database URL, API keys, JWT secret
```

No `.copilotignore`. No `CONVENTIONS.md`. No inline docstrings.

**Task:**

Score this repository against the 6-property AI-friendliness checklist. For each property, state: satisfied or not satisfied, and one specific finding that supports your rating. Then produce a ranked remediation list — most urgent first — with one sentence of justification per item.

**Expected answer:**

| Property | Satisfied? | Finding |
|----------|:----------:|---------|
| Clear naming | ❌ | `helpers.py` contains 6 distinct concern areas — no name can describe all of them; `api.py` mixes routing, serialization, auth, and error handling |
| Structured documentation | ❌ | `README.md` has no labelled sections; prose only — no `## What this does`, `## Setup`, `## Project structure` |
| Explicit conventions | ❌ | No `CONVENTIONS.md`; naming rules, import order, and commit format are undeclared |
| Scoped context | ❌ | No `.copilotignore`; `.env` with credentials has no context exclusion |
| Minimal redundancy | ⚠️ Partial | No dead code visible from file tree; `helpers.py` mixing multiple concerns creates conflation risk |
| Governed output | ❌ | No commit annotation convention; no review trail documented |

**Score: 0/6 — High-noise environment.**

**Ranked remediation list:**

1. **`.copilotignore` for `.env`** — Security-critical; a Restricted file in context is a compliance failure regardless of other properties.
2. **Split `helpers.py` into concern-scoped files** — Fixes Clear naming; reduces ambiguity amplification, which compounds with every session.
3. **Rewrite `README.md` with labelled sections** — Fixes Structured documentation; the README is read first in every session.
4. **Create `CONVENTIONS.md`** — Fixes Explicit conventions; prevents inconsistent naming in all future AI-assisted commits.
5. **Split `api.py` by concern** — Completes Clear naming fix; deferred because a file split requires dependency analysis first.
6. **Document commit annotation standard** — Fixes Governed output; lowest effort, can be documented before any code changes.

---

## Exercise 2 — README Reconstruction

**Type:** Rewrite
**Time:** ~10 minutes

**Context:**

The following README is the current documentation for a payment processing module:

```markdown
# Payment Module

This module handles everything related to payments for our e-commerce platform.
It was originally written by the backend team and has been updated several times
to support new payment providers. Currently we support Stripe and PayPal.

To use this module, make sure you have the right environment variables set.
The module needs `STRIPE_SECRET_KEY` and `PAYPAL_CLIENT_ID` set in your `.env`
file. Then you can import and call the functions as needed.

Known issues: sometimes the currency conversion fails for JPY, and there is a
race condition in the batch processing code that we haven't fixed yet.
```

**Task:**

Rewrite this README section using the AI-useful structure from this module. You do not need to invent content — use only information present in the original text. Acknowledge missing sections explicitly rather than filling them with invented facts.

**Expected answer:**

```markdown
## What this does

Handles payment processing for the e-commerce platform. Supports Stripe and PayPal.

## Setup

1. Set `STRIPE_SECRET_KEY` in `.env`.
2. Set `PAYPAL_CLIENT_ID` in `.env`.
3. Import and call functions as needed (see `## Project structure` — not yet documented).

## Project structure

*Not yet documented.*

## Conventions

*Not yet documented.* Link to `CONVENTIONS.md` when created.

## Known limitations

- Currency conversion fails for JPY — root cause not yet identified.
- Race condition in batch processing — fix not yet scheduled.

## Architecture notes

*Not yet documented.* Original authors: backend team.
```

**Why this is better than the original:**

- Each section is labelled — extractable by the AI without parsing prose.
- Known limitations are explicitly marked — prevents the AI from generating code that assumes those paths work correctly.
- Missing documentation is acknowledged as missing — prevents the AI from inventing it.

---

## Exercise 3 — Naming Convention Diagnosis

**Type:** Identification and rewrite
**Time:** ~10 minutes

**Context:**

A Python repository contains the following files. Each has a naming problem. Identify the violation for each file and propose a compliant replacement name with one sentence of reasoning.

| File | Current name | Contents |
|------|-------------|----------|
| A | `helpers.py` | Date formatting and timezone conversion |
| B | `do_stuff.py` | Validates user input for the registration form |
| C | `Manager.py` | Manages the database connection pool |
| D | `utils.py` | Generates PDF reports from invoice records |
| E | `handle_email.py` | Sends transactional email via SendGrid |
| F | `misc.py` | Contains 2 functions used only in `checkout.py` |

**Expected answer:**

| File | Violation | Replacement | Reasoning |
|------|-----------|-------------|-----------|
| A | Filler name — `helpers` describes nothing. | `date_formatters.py` | Names the single concern in the file. |
| B | Vague verb `do_stuff` — describes no domain. | `registration_validators.py` | Names the domain (registration) and the operation type (validators). |
| C | `PascalCase` for a module — Python convention is `snake_case` for file names. | `db_connection_pool.py` | snake_case; names the specific resource managed. |
| D | `utils` is a filler name; this file has one clear purpose. | `invoice_report_generator.py` | Names the input (invoice), output (report), and operation (generator). |
| E | `handle_` is a filler prefix — adds no meaning. | `transactional_email.py` | Names the concern (transactional email); the send method is implicit from file contents. |
| F | `misc` is the most ambiguous name in Python; contents belong in `checkout.py`. | Inline into `checkout.py` | Two functions used in one other file with no independent identity belong in that file, not in a separate module. |

---

## Exercise 4 — Governance Gap Analysis

**Type:** Evaluation
**Time:** ~15 minutes

**Context:**

A developer opens a pull request with the following commit message and diff summary:

```
commit a3f92c1
Author: Dev <dev@example.com>
Date:   Mon Apr 7 14:23:00 2026

    add password reset endpoint

diff --git a/api/auth.py b/api/auth.py
+def reset_password(user_email: str, new_password: str) -> bool:
+    user = db.find_by_email(user_email)
+    if user:
+        user.password = new_password
+        db.save(user)
+        return True
+    return False
```

No reviewer is named. No AI annotation is present. No test is included. The PR description reads: "adds password reset."

**Task:**

Identify every governance gap in this PR. For each gap, state which governance tier or protocol gate it violates and the specific risk if left unresolved. Then write a corrected commit message that addresses the gaps addressable at the commit message level.

**Expected answer:**

**Governance gaps:**

| Gap | Tier / Gate violated | Risk |
|-----|:--------------------:|------|
| No named reviewer | Merge annotation | No accountability for errors in `reset_password()`; undetectable in future audit |
| No AI-assisted annotation | Diff annotation | Cannot determine if this function was AI-generated; removes traceability |
| `new_password` stored without hashing (OWASP A02) | Pre-merge gate 4 | Plaintext password storage — critical security failure |
| No input validation on `user_email` or `new_password` (OWASP A03) | Pre-merge gate 4 | Injection risk; no length or format check on new password |
| No test included | Pre-merge gate 3 | Edge cases (empty email, empty password, user not found) are unverified |
| PR description has no acceptance criteria | Documentation quality | Cannot verify "done" without defined acceptance criteria |

**Corrected commit message:**

```
fix(auth): add password reset endpoint

NOTE: This commit as written is BLOCKED by pre-merge validation.
Failing gates:
- Gate 3: no test covers happy path or user-not-found path
- Gate 4: new_password stored without hashing (OWASP A02); no input
  validation (OWASP A03)

AI-assisted: [status unknown — no annotation; assume AI-assisted pending confirmation]
Reviewed-by: [required before merge]
```

---

## Exercise 5 — Pre-Merge Validation

**Type:** Application
**Time:** ~10 minutes

**Context:**

A Code Reviewer session produced the following function as a suggested fix for a failing test. Apply the 5-gate pre-merge validation protocol and produce a pass/fail result per gate.

```python
def get_user_data(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = db.execute(query)
    return result[0] if result else None
```

Context: the request was "fix the failing test for `get_user_data` — tests expect a single user dict or None."

**Expected answer:**

| Gate | Check | Result | Finding |
|------|-------|:------:|---------|
| 1. Scope | Does this diff contain exactly what was requested? | ✅ Pass | Returns a single user dict or None — matches the failing test requirement |
| 2. Ownership | Named human reviewer for AI-generated function? | ❌ Fail | No reviewer named; this is a direct Code Reviewer suggestion with no human review record |
| 3. Test coverage | Existing tests cover the changed lines? | ⚠️ Partial | The failing test covers the happy path; no test covers non-integer `user_id` or malicious input |
| 4. OWASP check | Passes 5-category OWASP minimum? | ❌ Fail | A03 — Injection: f-string interpolation of `user_id` directly into SQL. Fix: use a parameterized query: `db.execute("SELECT * FROM users WHERE id = ?", (user_id,))` |
| 5. Convention compliance | Complies with `CONVENTIONS.md`? | ⚠️ Unknown | Missing type annotations and docstring — cannot verify against conventions without access to `CONVENTIONS.md` |

**Overall result: BLOCKED** — Gate 4 failure (OWASP A03 — SQL Injection) is Critical severity. Gate 2 failure requires owner assignment before merge. Gates 3 and 5 require follow-up but do not independently block.
