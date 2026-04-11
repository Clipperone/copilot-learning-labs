# Lab 04 — Prompt Engineering Workshop

> **Paired module:** [Module 04 — Prompt Engineering for Coding](../../modules/04-prompt-engineering/)
> **Level:** Intermediate
> **Estimated time:** ~50 minutes
> **Prerequisites:** Module 04 complete · Lab 03 complete

---

## Objective

Apply the 4-component prompt structure to a real Python file with seven intentionally minimal functions — one per coding scenario. Then diagnose and rewrite three pre-written anti-pattern prompts. Finally, commit five working prompt templates to the shared prompt library.

By the end of this lab you will have:
- Applied each of the 7 coding scenario patterns from scratch.
- A written record of at least two anti-pattern diagnoses with rewrites.
- Five real, tested prompt library entries in `prompts/`.

---

## Before You Start

1. Open `labs/lab-04-prompt-engineering/starter/workbench.py` in VS Code.
2. Open the Copilot Chat panel (`Ctrl+Alt+I` / `Cmd+Alt+I`).
3. Keep [Module 04 README.md](../../modules/04-prompt-engineering/README.md) open as a reference tab.
4. Do not open `solution/workbench.py` before completing Task 1.

---

## The Workbench File

`starter/workbench.py` contains seven functions, each designed to exercise a specific prompt scenario.

| Function | Intentional gap | Target scenario |
|----------|-----------------|----------------|
| `parse_config(path)` | No type annotations, no validation, no error handling | Generation — add validation |
| `calculate_tax(amount, rate)` | Rate lookup mixed into the calculation logic | Refactoring — extract rate lookup |
| `merge_sorted(a, b)` | Off-by-one: skips the last element when lists are unequal length | Debugging — diagnose then fix |
| `apply_discount(price, code)` | No tests exist for this function | Testing — write pytest suite |
| `validate_email(address)` | No docstring | Documentation — write Google-style docstring |
| `check_permissions(user, resource)` | No OWASP review performed | Review — logic + OWASP A01 |
| `hash_password(plaintext)` | Uses MD5 — OWASP A02 violation | Security — diagnose exploit path + fix |

---

## Task 1 — Apply the First Four Scenarios (25 min)

Work through the first four functions using the prompt patterns from Module 04.

### 1a — Generation: `parse_config`

Write a prompt that asks Copilot to add:
- Type annotation for `path` and return type
- Validation that the file exists and raises `FileNotFoundError` with a descriptive message
- Returns a `dict` from the parsed TOML file

**Constraint discipline:** Ask for the function body only — no test code, no module-level imports beyond what the function needs.

**Expected output:** A function that raises `FileNotFoundError`, imports `pathlib.Path`, and returns `dict`.

---

### 1b — Refactoring: `calculate_tax`

Write a prompt that asks Copilot to extract the rate lookup into a separate `_get_tax_rate(rate_key: str) -> float` function.

**Constraint discipline:** State that the public interface of `calculate_tax` must not change. State that existing behavior must be preserved.

**Expected output:** Two functions — `_get_tax_rate` and a refactored `calculate_tax` that calls it.

---

### 1c — Debugging: `merge_sorted`

Write a two-prompt chain:
- **Prompt 1:** Ask for diagnosis only. Do not ask for a fix.
- **Prompt 2:** After confirming the root cause, ask for the fix.

**Constraint discipline:** In Prompt 1, end with "Do not propose a fix. Provide the diagnosis only."

**Expected output from Prompt 1:** Identification of the off-by-one index error when one list is exhausted before the other.
**Expected output from Prompt 2:** Corrected while-loop or slice-based tail append.

---

### 1d — Testing: `apply_discount`

Write a prompt that asks for a pytest suite covering:
- Valid discount code (any defined code in the function)
- Invalid discount code
- `price` of zero
- Negative `price`

**Constraint discipline:** One test function per case. Bare `assert` statements only. No `unittest.TestCase`.

**Expected output:** A test file with four named test functions.

---

## Task 2 — Apply the Last Three Scenarios (15 min)

### 2a — Documentation: `validate_email`

Write a prompt that produces a Google-style docstring for `validate_email`.

**Constraint discipline:** Audience is a developer who calls the function, not maintains it. Include `Args`, `Returns`, and `Raises`. No usage example.

---

### 2b — Review: `check_permissions`

Write a scoped code review prompt.

- Scope 1: Logic errors — any path that would grant or deny access incorrectly.
- Scope 2: OWASP A01:2021 — Broken Access Control.

Write two separate prompts, one for each scope. Compare the findings.

**Constraint discipline:** Each prompt must state explicitly what is out of scope.

---

### 2c — Security: `hash_password`

> ⚠️ **Premium model recommended:** Use o1 or Claude for this task. Exploit-path reasoning for cryptographic failures benefits from deeper analysis.

Write a security review prompt anchored to OWASP A02:2021 (Cryptographic Failures).

**Your prompt must:**
- State the runtime context: Python 3.11, no external auth library.
- Ask for the exploit path before the fix.
- Request: finding · exploit path · recommended fix · one code line showing the corrected implementation.

**Expected output:** Identification of MD5 as cryptographically broken, explanation of rainbow-table attack exposure, and a replacement using `hashlib.pbkdf2_hmac` or `bcrypt`.

Before accepting the fix, write the OWASP risk name in a comment on the line above the corrected call.

---

## Task 3 — Anti-pattern Diagnosis (5 min)

Each prompt below contains at least one anti-pattern from the Module 04 table. For each:
1. Name the anti-pattern.
2. Rewrite the prompt using the 4-component structure.
3. Note what different output you would expect.

**Prompt A:**
```
Look at my validate_email function. It has some issues with how it handles edge cases. Can you help me make it more robust and also add some tests while you're at it?
```

**Prompt B:**
```
Fix the security problem in hash_password.
```

**Prompt C:**
```
Here's my whole utils file. Review it and tell me everything that's wrong with it.
[paste of 250 lines]
```

---

## Task 4 — Commit Five Prompt Library Entries (5 min)

You now have five real, tested prompts from this lab. Formalize each one using [templates/prompt-template.md](../../templates/prompt-template.md) and save them to `prompts/`.

| Prompt | Save to |
|--------|---------|
| Testing prompt from Task 1d | `prompts/testing/write-tests.md` |
| Documentation prompt from Task 2a | `prompts/documentation/write-docstring.md` |
| Code review prompt from Task 2b | `prompts/review/code-review.md` |
| Security review prompt from Task 2c | `prompts/security/security-audit.md` |
| Migration prompt (write from scratch using the pattern in theory.md) | `prompts/migration/migrate-api.md` |

**Minimum content per file:**
- All header fields filled in — no `[PLACEHOLDER]` stubs remaining.
- A realistic filled-in example with actual input values.
- At least one row in the "Common Failures" table.

---

## Success Criteria

| Criterion | How to verify |
|-----------|--------------|
| `parse_config` handles missing file | Call it with a non-existent path — `FileNotFoundError` is raised with a message |
| `calculate_tax` is refactored | `_get_tax_rate` exists and `calculate_tax` calls it |
| `merge_sorted` bug is fixed | `merge_sorted([1,3], [2])` returns `[1,2,3]` |
| `apply_discount` has 4 tests | Run `pytest starter/` — 4 tests pass |
| `validate_email` has a docstring | Open the function — docstring is present in Google format |
| `hash_password` uses a secure algorithm | Function body no longer contains `md5`; uses `pbkdf2_hmac` or `bcrypt` |
| 5 prompt files exist in `prompts/` | Run `dir prompts/testing prompts/documentation prompts/review prompts/security prompts/migration` |
| No template stubs remain | Open each prompt file — no `[PLACEHOLDER]` text remains |

---

## Common Failure Points

| Failure | Cause | Recovery |
|---------|-------|---------|
| Copilot adds imports or module code you didn't ask for | Missing "function body only" constraint | Add explicit scope constraint; try again |
| Debugging prompt returns a fix before a diagnosis | Missed "diagnose only" constraint | Re-send with explicit constraint |
| Tests target implementation details instead of behavior | Prompt described the internals, not the contract | Rewrite prompt to describe input/output contract only |
| Security fix lacks context | No language/version in the prompt | Add Python version and library constraints |
| Prompt file still has `[PLACEHOLDER]` stubs | Template not completed | Fill every placeholder before saving |

---

## Solution Reference

After completing all tasks, compare your work to [solution/workbench.py](./solution/workbench.py).

The solution file shows one valid implementation for each function. Your implementations may differ — what matters is that the success criteria above are met.

---

## Completion

→ [checklist.md](./checklist.md) — Self-assessment before marking this lab complete

→ [Module 05 — Persistent Custom Instructions](../../modules/05-custom-instructions/) — The well-structured prompts from this lab become seed material for Module 05 instruction files.
