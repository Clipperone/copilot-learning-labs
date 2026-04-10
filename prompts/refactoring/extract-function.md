# Prompt: Extract a Function

> **Category:** refactoring
> **Difficulty:** basic
> **Works best with:** edit mode | inline chat
> **Premium model recommended:** no
> **Verified:** 2026-04

---

## Purpose

Extract a named block of code from an existing function into a standalone helper. Use when a function is too long or a section of logic is reused in multiple places.

---

## When to Use

- A function exceeds 30–40 lines and has distinct internal sections
- The same block of logic appears in 2 or more places
- A block of logic can be independently named and tested

**Do not use when:** the code block is tightly coupled to the caller's local state and cannot be cleanly separated without multiple parameters.

---

## The Prompt

```
Extract [DESCRIPTION_OF_BLOCK] from the [FUNCTION_NAME] function in [FILE_OR_SELECTION] into a new helper function.

Rules:
- Name the new function [NEW_FUNCTION_NAME] if I specify one, otherwise choose a descriptive name.
- Do not change the behavior of [FUNCTION_NAME] — it must call the new helper and produce identical results.
- [LANGUAGE] [VERSION]. Do not add imports unless necessary.
- Place the new function [PLACEMENT — e.g., "immediately above the caller" or "at the bottom of the file"].
- Include a type annotation on the new function.

Return both the modified [FUNCTION_NAME] and the new helper.
```

---

## Example Usage

### Input context

```python
def process_order(order: dict) -> dict:
    # Validate order
    if "id" not in order:
        raise ValueError("Order must have an id")
    if "items" not in order or not order["items"]:
        raise ValueError("Order must have at least one item")
    if "customer_id" not in order:
        raise ValueError("Order must have a customer_id")

    # Calculate total
    total = sum(item["price"] * item["quantity"] for item in order["items"])
    discount = 0.1 if total > 100 else 0
    total = total * (1 - discount)

    return {"order_id": order["id"], "total": total, "status": "processed"}
```

### Filled-in prompt

```
Extract the validation block (the three if/raise statements at the top) from the
`process_order` function in #selection into a new helper function.

Rules:
- Name the new function `validate_order`.
- Do not change the behavior of `process_order` — it must call `validate_order` first.
- Python 3.12. No new imports.
- Place the new function immediately above `process_order`.
- Include a type annotation: input is `dict`, return is `None` (it only raises).

Return both functions.
```

### Expected output

```python
def validate_order(order: dict) -> None:
    """Raise ValueError if the order is missing required fields."""
    if "id" not in order:
        raise ValueError("Order must have an id")
    if "items" not in order or not order["items"]:
        raise ValueError("Order must have at least one item")
    if "customer_id" not in order:
        raise ValueError("Order must have a customer_id")


def process_order(order: dict) -> dict:
    validate_order(order)

    total = sum(item["price"] * item["quantity"] for item in order["items"])
    discount = 0.1 if total > 100 else 0
    total = total * (1 - discount)

    return {"order_id": order["id"], "total": total, "status": "processed"}
```

---

## Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `[DESCRIPTION_OF_BLOCK]` | Plain-language description of the extracted block | `the input validation logic` |
| `[FUNCTION_NAME]` | The source function | `process_order` |
| `[FILE_OR_SELECTION]` | Scope of the edit | `#selection`, `#file:orders.py` |
| `[NEW_FUNCTION_NAME]` | Desired name for the helper (optional) | `validate_order` |
| `[PLACEMENT]` | Where to put the new function | `immediately above the caller` |

---

## Common Failures

| Failure | Cause | Fix |
|---------|-------|-----|
| Copilot extracts the wrong block | Description was ambiguous | Use `#selection` to select exactly the lines to extract |
| New function has too many parameters | Extracted block used too many caller-local variables | Accept the extra parameters, or reconsider whether extraction makes sense here |
| Original function behavior changes | Caller was not updated to call the helper | Add "return both the modified caller and new helper" |
| Missing type annotation | Constraint not stated | Add "include a type annotation on the new function" |
