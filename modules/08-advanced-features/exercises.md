# Module 08: Advanced Features in Copilot + VS Code — Exercises

Complete these exercises in order. Expected answers are provided after each exercise — work through the problem independently before reading the answer.

---

## Exercise 1 — Plan Mode Design Check

**Type:** Evaluation
**Time:** ~10 minutes

**Context:**

A developer used Plan mode on the following request:

> Add a `suspend_user(user_id)` function to `user_management.py` that marks a user as suspended and prevents them from logging in.

Plan mode returned this output:

> I'll add a `suspend_user()` function. The function should set a `suspended` flag on the user record. I'll modify `user_management.py` to add the function and update the `can_login()` check to respect the flag.

**Task:**

Evaluate this Plan output against the 5-element completeness checklist. Identify every missing element. For each, write the content the Plan output should include.

**Expected answer:**

| Element | Present? | Missing content |
|---------|:--------:|-----------------|
| 1. Problem restatement in AI's own words | ⚠️ Partial | Omits "prevents them from logging in" — should confirm `can_login()` returns `False` for suspended users |
| 2. Files to modify with reasoning | ⚠️ Partial | Lists `user_management.py` but gives no reasoning: e.g. "because both the data model and the login check live in this module" |
| 3. Proposed change per file (function scope, not line-by-line) | ⚠️ Partial | "Set a `suspended` flag" — does not describe where in the data model: dict field, dataclass field, or database column |
| 4. Statement of what will NOT change | ❌ Missing | Should say: "No other functions in `user_management.py` change. Token generation and password logic are out of scope." |
| 5. Open question if scope is ambiguous | ❌ Missing | Should say: "Confirm: does `suspended` need to persist across restarts, or is in-memory state sufficient for this session?" |

---

## Exercise 2 — Review Finding Triage

**Type:** Evaluation and rewrite
**Time:** ~15 minutes

**Context:**

A Code Reviewer session on a new `transfer_funds()` function produced these 6 findings. Classify each as actionable or non-actionable. For non-actionable findings, rewrite them to be actionable.

| # | Finding as written |
|---|-------------------|
| 1 | "The code looks risky." |
| 2 | "High — `transfer_funds()` in `banking.py`, line 42: `amount` is not validated before subtraction. A negative value reverses the transfer direction. Fix: add `if amount <= 0: raise ValueError('amount must be positive')` at the function entry." |
| 3 | "You should add tests." |
| 4 | "Medium — `banking.py`, line 58: no explicit rollback if the credit step fails after the debit step completes. Partial transfer is possible. Fix: wrap both steps in a transaction or add a compensating operation." |
| 5 | "Critical — `banking.py`: possible security issue with the user input." |
| 6 | "Low — `transfer_funds()` docstring is missing the `Raises` section. Fix: add `Raises: ValueError if amount <= 0; PermissionError if sender balance is insufficient.`" |

**Expected answer:**

| # | Actionable? | Reason / Rewrite |
|---|:-----------:|------------------|
| 1 | ❌ | No severity, no location, no description, no fix. Rewrite requires identifying the specific risk: e.g. "High — `banking.py`, `transfer_funds()`: no input validation on `amount`. [line] [description] [fix]." |
| 2 | ✅ | Severity, file, line, description, and fix are all present. |
| 3 | ❌ | No scope, no coverage gap identified, no specific test target. Rewrite: "Low — `banking.py`, `transfer_funds()`: no test covers the negative-amount path. Add one test confirming `ValueError` is raised when `amount <= 0`." |
| 4 | ✅ | Severity, file, line, failure mode, and fix are all present. |
| 5 | ❌ | "Critical" stated but no line, no description of the issue, no exploit path, no fix. Rewrite requires identifying the exact line, the input handling failure, and the OWASP category. |
| 6 | ✅ | Severity, location (function name), description, and fix are present. |

---

## Exercise 3 — Terminal Command Validation

**Type:** Application
**Time:** ~10 minutes

**Context:**

A developer asked `@terminal` to generate commands for four tasks. Apply the 4-question gate to each command. State whether you would run it and why.

| # | AI-generated command | Task asked |
|---|---------------------|-----------|
| 1 | `git reset --hard HEAD~3` | "Undo the last 3 commits on my local branch" |
| 2 | `pytest tests/ -v` | "Run all tests with verbose output" |
| 3 | `find . -name "*.pyc" -delete` | "Delete compiled Python files" |
| 4 | `git push --force origin main` | "Push my changes to the main branch" |

**Expected answer:**

| # | Run? | Reasoning |
|---|:----:|-----------|
| 1 | ⚠️ With caution | Does what was asked. Side effect: irreversible loss of 3 local commits if not already pushed — recoverable only via `git reflog`. Verify with `git log` before running. |
| 2 | ✅ | Does what was asked. No side effects. Reversible (nothing changes). Low risk. |
| 3 | ⚠️ With caution | Does what was asked. Side effect: deletes `.pyc` files recursively from current directory. Reversible (regenerate on next run), but confirm working directory is the repo root before running. |
| 4 | ❌ | Does what was asked — and overwrites the remote `main` branch irreversibly for all collaborators. Never run without explicit team agreement. This command fails the accountability test for any shared repository. |

---

## Exercise 4 — Sensitivity Classification

**Type:** Application
**Time:** ~10 minutes

**Context:**

A project has the following file tree. Classify each item by sensitivity level (Public / Internal / Confidential / Restricted) and state which items to add to `.copilotignore`.

```
project/
├── README.md
├── .env
├── config/
│   ├── settings.py              # reads from .env; builds DB connection string
│   └── test_settings.py        # overrides settings with in-memory values for tests
├── src/
│   ├── api/
│   │   └── payments.py         # Stripe API integration; formats charge requests
│   └── utils/
│       └── encrypt.py          # AES-256 encryption/decryption utilities
├── tests/
│   └── test_payments.py        # tests using mock Stripe responses; no real keys
└── infra/
    └── deploy.sh               # CI script that calls AWS CLI with role assumption
```

**Expected answer:**

| Path | Level | Reason |
|------|-------|--------|
| `README.md` | Public | Documentation; no sensitive data |
| `.env` | Restricted | Real credentials; never in any AI context; add to `.copilotignore` immediately |
| `config/settings.py` | Confidential | Constructs DB connection strings; session allowed; never paste verbatim into chat |
| `config/test_settings.py` | Internal | Test overrides only; no real credentials |
| `src/api/payments.py` | Confidential | Payment integration logic; review findings must not be shared externally without redaction |
| `src/utils/encrypt.py` | Confidential | Cryptographic logic; OWASP A02 in scope; same classification as auth files |
| `tests/test_payments.py` | Internal | Mock data only; no real keys or PII |
| `infra/deploy.sh` | Confidential | AWS CLI with role assumption; infrastructure-scope operations |

`.copilotignore` additions: `.env` (Restricted); consider adding `infra/deploy.sh` if role credential strings appear inline.

---

## Exercise 5 — OWASP Gate

**Type:** Analysis and fix
**Time:** ~10 minutes

**Context:**

A developer committed the following function. A Code Reviewer session has flagged it — but produced no specific findings yet. Identify the OWASP Top 10 issues present. For each, name the category, describe the exploit path if left unfixed, and state the minimum fix.

```python
import sqlite3

def get_user(username: str) -> dict | None:
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "username": row[1], "password_hash": row[2]}
    return None
```

**Expected answer:**

| Issue | OWASP Category | Exploit path | Minimum fix |
|-------|---------------|-------------|-------------|
| f-string SQL construction | A03 — Injection | `username = "' OR '1'='1"` returns all records without authentication; `"'; DROP TABLE users; --"` truncates the table | Use parameterized query: `cursor.execute("SELECT * FROM users WHERE username = ?", (username,))` |
| `password_hash` in return value | A02 — Cryptographic Failures (exposure) | Callers who serialize the dict to an API response or log it expose the hash; hash exposure assists offline cracking | Remove `"password_hash": row[2]` from the returned dict; return only `id` and `username` |
| No input validation on `username` | A03 — Injection (contributing) | Empty string or very long input causes unexpected query behavior or a database error that may leak schema information | Add `if not username or not isinstance(username, str): raise ValueError("username required")` before the query |
