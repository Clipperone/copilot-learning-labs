# Prompt: Refactor a Function for Clarity

> **Category:** refactoring
> **Difficulty:** basic
> **Works best with:** agent mode | inline chat
> **Premium model recommended:** no
> **Verified:** 2026-04

---

## Purpose

Improve the internal structure of a function without changing its external behavior. Use when a function is correct but hard to read, deeply nested, or uses unclear names.

---

## When to Use

- A function is working but difficult to understand or maintain
- Nesting is more than 2 levels deep
- Variable names are unclear or abbreviated
- The function mixes multiple concerns

**Do not use when:** you also want to change the function's behavior. Separate refactoring from feature changes — do them in distinct prompts.

---

## The Prompt

```
Refactor the [FUNCTION_NAME] function in [FILE_OR_SELECTION] for clarity.

Rules:
- Do not change the function signature or return type.
- Do not change behavior — input/output mapping must stay identical.
- [LANGUAGE] [VERSION] — do not introduce libraries not already imported.
- Preserve all existing comments that explain business logic.

Improvements to make:
- [IMPROVEMENT_1 — e.g., "Extract the validation logic into a helper function."]
- [IMPROVEMENT_2 — e.g., "Replace abbreviated variable names with descriptive ones."]
- [IMPROVEMENT_3 — e.g., "Replace the nested if/else with early returns."]

Return only the refactored function. Do not rewrite the full file.
```

---

## Example Usage

### Input context

```python
def proc(d, t, x):
    if d is not None:
        if len(d) > 0:
            if t == "A":
                res = []
                for i in d:
                    if i > x:
                        res.append(i * 2)
                return res
            else:
                return d
        else:
            return []
    else:
        return None
```

### Filled-in prompt

```
Refactor the `proc` function in #selection for clarity.

Rules:
- Do not change the function signature or return type.
- Do not change behavior — input/output must stay identical.
- Python 3.12. No new imports.
- Preserve any comments that explain business logic.

Improvements to make:
- Replace `proc`, `d`, `t`, `x`, `res`, `i` with descriptive names that reflect their roles.
- Replace nested if/else with early returns where possible.
- Extract the filtering-and-doubling loop into a helper if it improves readability.

Return only the refactored function.
```

### Expected output

```python
def filter_and_double(items: list[int] | None, mode: str, threshold: int) -> list[int] | None:
    if items is None:
        return None
    if not items:
        return []
    if mode != "A":
        return items
    return [item * 2 for item in items if item > threshold]
```

---

## Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `[FUNCTION_NAME]` | The exact name of the function to refactor | `calculate_discount` |
| `[FILE_OR_SELECTION]` | File reference or `#selection` | `#file:orders.py` or `#selection` |
| `[LANGUAGE] [VERSION]` | Language and version constraint | `Python 3.12`, `TypeScript 5.4` |
| `[IMPROVEMENT_1..N]` | Specific, targeted changes — one per bullet | `Replace early exit with guard clauses` |

---

## Common Failures

| Failure | Cause | Fix |
|---------|-------|-----|
| Copilot changes behavior | Prompt did not explicitly state "do not change behavior" | Add the constraint explicitly |
| Copilot rewrites the entire file | `[FILE_OR_SELECTION]` referenced the whole file | Use `#selection` to scope to the single function |
| Copilot introduces new libraries | No constraint on imports | Add "do not introduce libraries not already imported" |
| Variable names not improved | Improvements not listed explicitly | List the specific names to change: "Rename `d` to `items`" |
