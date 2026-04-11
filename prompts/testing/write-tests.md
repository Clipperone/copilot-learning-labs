# Prompt: Testing — Write a Pytest Suite for an Existing Function

> **Category:** testing
> **Difficulty:** intermediate
> **Works best with:** ask mode | inline chat
> **Premium model recommended:** no
> **Verified:** 2026-04

---

## Purpose

Write a complete pytest suite for an existing Python function, covering the explicit edge cases you provide.

---

## When to Use

- You have a function with no tests and want to add coverage fast.
- You want to ensure specific edge cases are covered rather than leaving them to Copilot's judgment.
- You are adding tests before a refactoring to protect the existing behavior.

**Do not use when:** the function does not yet exist. Use the generation prompt to write the function first; then use this prompt for the tests.

---

## The Prompt

```
Task: Write pytest tests for `[FUNCTION_NAME]([FUNCTION_SIGNATURE])`.
Constraints: Cover these cases: [EDGE_CASE_LIST]. One test function per case. Use bare `assert` statements — no `unittest.TestCase`. Do not test implementation details — test the input/output contract.
Output: Test file content only, starting from the import line.
```

---

## Example Usage

### Input context

```python
DISCOUNT_CODES = {
    "SAVE10": 0.10,
    "HALF": 0.50,
}

def apply_discount(price: float, code: str) -> float:
    discount = DISCOUNT_CODES.get(code, 0.0)
    return round(price * (1 - discount), 2)
```

### Prompt (filled in)

```
Task: Write pytest tests for `apply_discount(price: float, code: str) -> float`.
Constraints: Cover these cases: valid discount code "SAVE10", invalid discount code, price of zero, negative price. One test function per case. Use bare `assert` statements — no `unittest.TestCase`. Do not test implementation details — test the input/output contract.
Output: Test file content only, starting from the import line.
```

### Expected output

```python
import pytest
from workbench import apply_discount


def test_valid_discount_code():
    assert apply_discount(100.0, "SAVE10") == 90.0


def test_invalid_discount_code():
    assert apply_discount(100.0, "INVALID") == 100.0


def test_price_of_zero():
    assert apply_discount(0.0, "SAVE10") == 0.0


def test_negative_price():
    assert apply_discount(-50.0, "SAVE10") == -45.0
```

---

## Variables to Customize

| Placeholder | What to put here | Example |
|-------------|-----------------|---------|
| `[FUNCTION_NAME]` | The exact function name | `apply_discount` |
| `[FUNCTION_SIGNATURE]` | Parameters and return type | `price: float, code: str) -> float` |
| `[EDGE_CASE_LIST]` | A comma-separated list of specific cases | `valid code, invalid code, zero price, negative price` |

---

## Tips

- Always list edge cases explicitly. Copilot defaults to happy-path coverage only.
- If the function raises exceptions, add "raises [ExceptionType] when [condition]" to the edge case list.
- After running the tests, verify that each assertion is testing the behavior you intended — not an implementation detail.

## Common Failures

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Only one or two tests generated | Edge case list too vague | List each case explicitly rather than describing categories |
| Tests use `unittest.TestCase` | Constraint missing | Add "Use bare `assert` statements — no `unittest.TestCase`" |
| Tests import from wrong module | Module path not specified | Add `Context: function is in [MODULE_PATH]` before the Task line |

---

## Related Prompts

- [prompts/generation/generate-function.md](../generation/generate-function.md) — Generate the function before writing tests
- [prompts/review/code-review.md](./code-review.md) — Review test coverage after generating the suite
