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

---

## Exercise 6 — Plan → Implementer Handoff

**Type:** Application (integration)
**Time:** ~20 minutes

**Context:**

You used Plan mode and received a complete 5-element plan. You now need to open an Implementer session that executes exactly that plan — no more, no less. This exercise tests whether you can convert Plan output into a bounded Implementer initialization and verify the result matches the plan.

**Plan output (assume this passed the 5-element completeness check from Exercise 1):**

```text
Problem: Add a `suspend_user(user_id)` function to user_management.py that marks
         a user as suspended and prevents login. Must persist across restarts
         (confirmed with PM — use the existing `users` SQLite table).

Files to modify:
  - user_management.py  — add function + update can_login()
  - migrations/0007_add_suspended_flag.sql  — new migration for the column

Proposed change per file:
  - user_management.py: add `suspend_user(user_id: int) -> None` that updates
    `users.suspended = 1` for the given id. Modify `can_login(user_id)` to
    return False when `suspended = 1`.
  - migrations/0007_add_suspended_flag.sql: ALTER TABLE users ADD COLUMN
    suspended INTEGER NOT NULL DEFAULT 0.

Will NOT change:
  - Token generation, password hashing, session management.
  - Any callers of `can_login()` — they remain source-compatible.

Open question (resolved): persistence confirmed; use the existing DB.
```

**Task:**

1. Write the **Implementer initialization prompt** that opens a new Agent session bounded to this plan. The prompt must:
   - State the scope as **"Implement the plan below — nothing outside it"** and paste the plan verbatim.
   - Name the two files that may be edited; forbid edits to any other file.
   - Name the exit condition: both files compiled/applied + `can_login()` returns `False` for a suspended user in a smoke test.
   - Exclude test authoring from this session (that belongs to a Test Engineer handoff).

2. Write the **3-item verification checklist** you will run against the Implementer's diff before closing the session. Each item must reference a specific element of the plan.

3. **Drift diagnosis:** The Implementer returns a diff that (a) adds the column, (b) adds `suspend_user()`, (c) updates `can_login()`, and (d) also modifies `token.py` to invalidate active tokens for suspended users. Which element of the plan does (d) violate? What do you do — accept, reject, or replan? State your reasoning in one sentence.

**Expected answer:**

1. **Initialization prompt shape** — must contain: verbatim plan quote, scope sentence, file allowlist (`user_management.py`, `migrations/0007_add_suspended_flag.sql`), exit condition (migration applied + smoke test passes), and exclusion ("Do not write tests; do not modify other files").

2. **Verification checklist:**
   - [ ] `suspend_user(user_id)` exists with the signature named in the plan; updates `users.suspended = 1` via parameterized query.
   - [ ] `can_login()` returns `False` when `suspended = 1`; returns previous behavior otherwise.
   - [ ] The migration file `0007_add_suspended_flag.sql` matches the proposed `ALTER TABLE` statement exactly; no other migrations added.

3. **Drift diagnosis:** (d) violates the plan's **"Will NOT change"** clause — `token.py` was explicitly out of scope. Reject the diff, close the session, and either (i) replan to include token invalidation as a second task with its own Plan→Implementer cycle, or (ii) accept the original 3-file diff and open a new plan for token invalidation. Do not accept (d) silently — silent scope creep is the failure mode this boundary prevents.

> **Why this matters:** The Plan mode → Implementer handoff is the concrete form of the Planner → Implementer pattern from Module 07. Treating the plan as a contract (not a suggestion) is what makes multi-agent workflows deterministic.

---

## Exercise 7 — Edits-Style Coordinated Refactor in Agent Mode

**Type:** Application
**Time:** ~15 minutes

**Context:**

Edit mode was consolidated into Agent mode in VS Code 1.110. This exercise rebuilds the Edit-mode contract — bounded multi-file diff, no terminal, per-file review — using only Agent mode discipline.

**Setup:**

Create three files in a scratch folder:

```python
# user_model.py
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
```

```python
# user_service.py
from user_model import User

def get_user(id):
    return User(id, "Alice")
```

```python
# test_user_service.py
from user_service import get_user

def test_get_user():
    user = get_user(1)
    assert user.name == "Alice"
```

**Task:**

Open Agent mode and rename `id` → `user_id` across all three files in a single coordinated session. Your initialization prompt must enforce the Edits-style discipline:

1. Reference all three files explicitly with `#file:`.
2. State: *"Do not run terminal commands. Do not run tests. Produce a diff only."*
3. State: *"Edit only the three files I named. Do not create new files."*
4. State the exit condition: every occurrence of `id` referring to the user identifier is renamed to `user_id`; built-in `id()` (if present) is left alone.

After Agent produces the diff:

- Review each file's diff independently (do not "Accept all").
- Reject any change that touches a file outside the three named, or that renames a non-user `id`.
- Accept the rest.
- Run the test manually after accepting; it must still pass.

**Self-check:**

- [ ] Initialization prompt named all three files with `#file:`.
- [ ] Initialization prompt explicitly disabled terminal and forbade out-of-scope edits.
- [ ] You reviewed and accepted per-file (not "Accept all").
- [ ] The test still passes after the rename.
- [ ] If you re-ran this rename next month on different files, you could either copy the prompt or save it as a custom agent. State which you'd choose and why.

> **Bonus:** Convert your initialization prompt into a custom agent file (`.github/agents/refactor-coordinator.agent.md`) following the Module 08 theory example. Re-run the exercise on a second rename (`name` → `display_name`) using `@refactor-coordinator`. Compare the discipline you had to enforce manually vs. what the custom agent enforced automatically.

---

## Exercise 8 — Configure One MCP Server

**Type:** Application
**Time:** ~20 minutes

**Context:**

This exercise introduces the Model Context Protocol by configuring the smallest useful MCP server (`@modelcontextprotocol/server-filesystem`) and verifying its scope boundary. The goal is not to build a server — it is to understand the contract well enough to evaluate any MCP server you might add later.

**Setup:**

1. Create a sandbox directory at the repo root: `scratch/`. Add two files: `notes.txt` (a few lines of text), `todos.txt` (a few bullets).
2. Create `.vscode/mcp.json`:

    ```json
    {
      "servers": {
        "filesystem": {
          "command": "npx",
          "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "${workspaceFolder}/scratch"
          ],
          "transport": "stdio"
        }
      }
    }
    ```

3. Restart VS Code's chat session.

**Task:**

1. **Tool discovery.** In Agent mode, ask: *"What tools does the `filesystem` MCP server expose? List each tool with its parameters."* Save the answer.
2. **In-scope read.** Ask: *"Using the filesystem MCP server, list the files in scratch/ and show me the first 3 lines of each."* Verify you get content from both files.
3. **In-scope write.** Ask: *"Using the filesystem MCP server, append the line `verified` to `scratch/todos.txt`."* Verify the file changed on disk.
4. **Scope boundary test.** Ask: *"Using the filesystem MCP server, read `package.json` from the repo root."* The server **must** refuse — `package.json` is outside the configured scope. If the agent reads it, your `mcp.json` scope is wrong. Fix it before proceeding.
5. **Trace inspection.** Open the chat output for steps 2–4. Identify (a) the server name, (b) the tool name, (c) the arguments passed, (d) the return value. This is the JSON-RPC contract.

**Self-check:**

- [ ] `mcp.json` exists at `.vscode/mcp.json` with scope set to a sub-directory, **not** repo root.
- [ ] Agent successfully completed steps 2 and 3 (in-scope operations).
- [ ] Agent **refused** step 4 (out-of-scope read).
- [ ] You can name the 4 fields of any tool call from the trace (server, tool, arguments, result).
- [ ] You can state in one sentence when MCP is the right answer vs. a custom agent vs. an instruction file vs. a prompt file.

**Deliverable:** Commit `.vscode/mcp.json` plus a short `mcp-trace.md` containing one of the JSON-RPC traces you observed and your one-sentence answer to the last self-check item.

> **Anti-pattern check:** If you scoped the server to `${workspaceFolder}` (repo root), your sandbox would have included `.env`, `.git`, and any other sensitive files. The whole point of MCP scope is to make that mistake explicit and configurable. Never repo-root by default.
