# Module 04 — Exercises

These exercises build the 4-component prompt structure into muscle memory. Each exercise is self-contained — complete them in the order listed or skip to the scenario you need most.

Complete all exercises before moving to Lab 04. The lab applies these skills to a single workbench file under time pressure.

---

## Exercise 1 — Spot the Missing Component

**Objective:** Identify which prompt component is absent.

Read each prompt below. State which of the four components is missing (Task · Role · Constraints · Output format) and explain why its absence will cause a poor result.

**Prompt A:**
```
Add error handling to this function.
```

**Prompt B:**
```
Role: Act as a Python expert.
Task: Rewrite the `calculate_tax` function.
Output: The refactored function only.
```

**Prompt C:**
```
Task: Write tests for `validate_email`.
Constraints: Use pytest. Cover null, empty string, and valid input.
```

**Expected outcomes:**
- A: Missing constraints (what errors to handle, what to return on error) and output format.
- B: Missing constraints (what to change, what must not change).
- C: Missing output format (file content? specific function names? assertion style?).

---

## Exercise 2 — Rewrite an Anti-pattern

**Objective:** Convert vague prompts into structured ones.

Rewrite each prompt using the 4-component pattern. Include at least one constraint that prevents common over-generation.

**Prompt A — Double task:**
```
Fix the off-by-one bug in merge_sorted and write tests for it.
```

**Prompt B — Context dump:**
```
Here is my entire utils.py file. Can you check if there are any issues?
```

**Prompt C — Premature fix:**
```
The hash_password function is broken. What should I change it to?
```

**Guidance:**
- A: Split into two sequential prompts. Prompt 1 = diagnose/fix. Prompt 2 = test the fixed version.
- B: Identify the specific concern (logic errors? OWASP? style?). Scope to one function.
- C: Ask for diagnosis and exploit path before the fix. Add OWASP A02 as the review scope.

---

## Exercise 3 — Generate a Reusable Template

**Objective:** Turn a one-off prompt into a parameterized template.

Start with this working prompt:
```
Task: Write pytest tests for `validate_email(address: str) -> bool`.
Constraints: Cover these cases: None input, empty string, missing @, valid address. One test per case. Use bare assert statements.
Output: Test file content starting from the import line.
```

Rewrite it as a reusable template following the `[PLACEHOLDER]` convention. Every value that would change when testing a different function must become a placeholder.

**Minimum required placeholders:** `[FUNCTION_NAME]`, `[FUNCTION_SIGNATURE]`, `[EDGE_CASE_LIST]`

**Verify your template** by filling in the placeholders for a second function of your choice and confirming the prompt still makes sense.

---

## Exercise 4 — Apply the Security Scenario

**Objective:** Write a full security review prompt anchored to OWASP.

The following function uses MD5 to hash passwords:

```python
import hashlib

def hash_password(plaintext: str) -> str:
    return hashlib.md5(plaintext.encode()).hexdigest()
```

Write a security review prompt that:
- Anchors to OWASP A02:2021 (Cryptographic Failures)
- States the runtime context: Python 3.11, no external auth library
- Asks for the exploit path before the fix
- Requests a one-line code example of the corrected implementation

**Checklist for your prompt:**
- [ ] Role line specifies security engineering perspective
- [ ] OWASP category named explicitly
- [ ] Language + version stated
- [ ] "Describe exploit path before fix" constraint present
- [ ] Output format names the four deliverables

---

## Exercise 5 — Make the Premium Model Decision

**Objective:** Assign the correct model tier to each scenario.

For each task below, state: **Default** or **Premium** — and give a one-sentence reason.

| Task | Your answer | Reason |
|------|-------------|--------|
| Write a Google-style docstring for `apply_discount` | | |
| Debug a race condition in an async task queue | | |
| Generate a pytest suite for `parse_config` | | |
| Perform an OWASP A02 security audit on `hash_password` | | |
| Refactor `calculate_tax` to extract the rate lookup | | |
| Migrate 15 call sites from `requests` to `httpx` | | |

**Reference answers:**

| Task | Answer | Reason |
|------|--------|--------|
| Write a Google-style docstring for `apply_discount` | Default | Language generation; no multi-step reasoning |
| Debug a race condition in an async task queue | Premium | Concurrent causal reasoning requires depth |
| Generate a pytest suite for `parse_config` | Default | Mechanical coverage expansion |
| Perform an OWASP A02 security audit on `hash_password` | Premium | Exploit-path reasoning justified |
| Refactor `calculate_tax` to extract the rate lookup | Default | Structural, not semantic |
| Migrate 15 call sites from `requests` to `httpx` | Default or GPT-4o | Depends on call-site complexity |

---

## Exercise 6 — Promote a Markdown Prompt to a `.prompt.md` File

**Objective:** Convert one prompt from the [`prompts/`](../../prompts/) library into a runnable `.prompt.md` file with variables; invoke it twice with different inputs; verify substitution.

**Pick one source prompt** (any will do):

- [`prompts/refactoring/extract-function.md`](../../prompts/refactoring/extract-function.md)
- [`prompts/testing/write-tests.md`](../../prompts/testing/write-tests.md)
- [`prompts/documentation/write-docstring.md`](../../prompts/documentation/write-docstring.md)

**Task:**

1. Copy the prompt body to `.github/prompts/[verb-object].prompt.md`.
2. Convert each `[PLACEHOLDER]` to `${input:placeholderName}`. Use camelCase for the variable names.
3. Add frontmatter:
   - `mode` — `ask` or `agent`, matching the source prompt's recommended mode.
   - `description` — one sentence shown in the `/` picker.
   - `model` — only if the source prompt explicitly recommends a premium model.
   - `tools` — only if `mode: agent` and you need to scope tools.
4. Invoke the prompt in chat with `/[name]`. Provide one set of inputs.
5. Invoke it again with a different set of inputs. Confirm both runs produced output appropriate to their inputs.

**Self-check:**

- [ ] The frontmatter has `mode` and `description` at minimum.
- [ ] Every `${input:...}` matches a variable that actually changes between the two runs.
- [ ] The two runs produced visibly different output (proving substitution worked).
- [ ] No secrets, internal hostnames, or temporary task context in the body.
- [ ] The description clearly states the action; a teammate could pick it from the `/` list without opening the file.

**Deliverable:** Commit the new `.prompt.md` file plus a short note (in the commit message or a `RUN.md`) showing the two invocations and their inputs.

> **Anti-pattern check:** If you find yourself writing a prompt body longer than ~150 lines or describing two unrelated objectives, split it. One prompt file = one named action.

---

## Navigation

← [README.md](./README.md) — Module overview and scenario reference

→ [checklist.md](./checklist.md) — Self-assessment before moving to the lab

→ [Lab 04](../../labs/lab-04-prompt-engineering/) — Apply all seven scenarios under lab conditions
