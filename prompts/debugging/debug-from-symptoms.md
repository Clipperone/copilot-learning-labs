# Prompt: Debug from Symptoms

> **Category:** debugging
> **Difficulty:** basic
> **Works best with:** ask mode
> **Premium model recommended:** no (use premium for complex async/concurrency bugs)
> **Verified:** 2026-04

---

## Purpose

Diagnose a bug by describing what is happening, what you expected, and what the code does. Use before asking Copilot to fix anything — get an explanation first.

---

## When to Use

- The code runs but produces wrong results
- An error or exception is thrown and you don't understand why
- Behavior is inconsistent or environment-dependent

**Do not use when:** you already know the root cause and just need a fix — use the inline chat fix prompt instead.

---

## The Prompt

```
I have a bug in the following [LANGUAGE] code. Help me diagnose it.

**What I expected:**
[EXPECTED_BEHAVIOR]

**What actually happens:**
[ACTUAL_BEHAVIOR — include error message or wrong output verbatim]

**Code:**
```[LANGUAGE]
[PASTE_CODE_HERE]
```

**Context:**
- Language / runtime version: [VERSION]
- Relevant dependencies: [LIBRARY_NAME_AND_VERSION or "none"]
- Input I used when the bug occurred: [INPUT_EXAMPLE]

Do not fix the code yet. First explain:
1. What the root cause is
2. Why the code behaves this way
3. What the fix should be at a conceptual level
```

---

## Example Usage

### Input context

*(code that has a bug)*

### Prompt (filled in)

```
I have a bug in the following Python code. Help me diagnose it.

**What I expected:**
The function should return a list with duplicate values removed, preserving the original order.

**What actually happens:**
The order of items changes in the output sometimes, especially on Python 3.6.

**Code:**
```python
def remove_duplicates(items):
    return list(set(items))
```

**Context:**
- Language / runtime version: Python 3.6
- Relevant dependencies: none
- Input I used when the bug occurred: ['b', 'a', 'c', 'a', 'b']

Do not fix the code yet. First explain:
1. What the root cause is
2. Why the code behaves this way
3. What the fix should be at a conceptual level
```

### Expected output

Copilot should explain that:
1. `set` does not preserve insertion order
2. In Python 3.6, `dict` preserves insertion order but `set` does not guarantee it
3. The fix is to use `dict.fromkeys()` instead of `set()`

---

## Variables to Customize

| Placeholder | What to put here | Example |
|-------------|-----------------|---------|
| `[LANGUAGE]` | Programming language | `Python` |
| `[EXPECTED_BEHAVIOR]` | What should happen | `return deduplicated list preserving order` |
| `[ACTUAL_BEHAVIOR]` | What actually happens | `order changes on Python 3.6` |
| `[PASTE_CODE_HERE]` | The buggy code | *(the function)* |
| `[VERSION]` | Runtime version | `Python 3.6` |
| `[INPUT_EXAMPLE]` | The input that triggers the bug | `['b', 'a', 'c', 'a', 'b']` |

---

## Tips

- Always include the error message verbatim if one exists — Copilot uses the exact text to identify the cause.
- Always specify the version. The same code can behave differently across versions.
- Ask for explanation before fix — it's faster to confirm you understood the root cause than to blindly apply a fix and have it reappear.
- After getting the explanation, follow up: `Now show me the fix and explain why it resolves the root cause.`

## Common Failures

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Copilot jumps straight to fixing | Prompt didn't say "do not fix yet" | Include that instruction explicitly |
| Explanation is too generic | Error message not included | Add the exact error/output verbatim |
| Wrong diagnosis | Missing version or dependency context | Add all context fields |

---

## Related Prompts

- [generate-function.md](../generation/generate-function.md) — when you need to rewrite the function after diagnosis
