# Prompt: Documentation — Write a Google-Style Docstring

> **Category:** documentation
> **Difficulty:** basic
> **Works best with:** inline chat | ask mode
> **Premium model recommended:** no
> **Verified:** 2026-04

---

## Purpose

Write a Google-style docstring for an existing Python function, targeting the developer who calls the function — not one who maintains it.

---

## When to Use

- A function has no docstring and you are adding one before a code review.
- You are enforcing a consistent docstring style across a module.
- You want a docstring that covers Args, Returns, and Raises without a verbose usage example.

**Do not use when:** you need module-level or class-level documentation. Scope this prompt to one function at a time.

---

## The Prompt

```
Task: Write a Google-style docstring for `[FUNCTION_NAME]`.
Constraints: Audience is a developer who calls this function, not one who maintains it. Include: Args, Returns, Raises. Do not include a usage example. Docstring must not restate the function name as its summary line.
Output: The docstring only, inside triple quotes.
```

---

## Example Usage

### Input context

```python
def validate_email(address: str) -> bool:
    if not isinstance(address, str):
        return False
    if "@" not in address:
        return False
    parts = address.split("@")
    if len(parts) != 2:
        return False
    local, domain = parts
    if not local or not domain:
        return False
    if "." not in domain:
        return False
    return True
```

### Prompt (filled in)

```
Task: Write a Google-style docstring for `validate_email`.
Constraints: Audience is a developer who calls this function, not one who maintains it. Include: Args, Returns, Raises. Do not include a usage example. Docstring must not restate the function name as its summary line.
Output: The docstring only, inside triple quotes.
```

### Expected output

```python
"""Validate that a string is a minimally well-formed email address.

Checks for the presence of exactly one `@` separator and a domain
containing at least one `.`. Does not perform DNS or MX record lookup.

Args:
    address: The string to validate. Must be a `str` instance.

Returns:
    `True` if the address passes all format checks, `False` otherwise.

Raises:
    No exceptions. Returns `False` for all non-string or malformed inputs.
"""
```

---

## Variables to Customize

| Placeholder | What to put here | Example |
|-------------|-----------------|---------|
| `[FUNCTION_NAME]` | The exact function name | `validate_email` |

---

## Tips

- Paste the full function body when using inline chat so Copilot can infer the behavior accurately.
- If the function raises multiple exception types, list each one explicitly: "Add: `ValueError` when X, `TypeError` when Y."
- For async functions, add "Note: this is an async function" to the constraints line.

## Common Failures

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Summary line restates the function name ("Validate email address.") | Missing "must not restate the function name" constraint | Add the constraint explicitly |
| Docstring includes a usage example | Missing "no usage example" constraint | Add the constraint or delete the example section |
| Returns section says "bool" instead of describing the semantics | Default behavior — Copilot echoes the type annotation | Ask for a narrative Returns description: "what True means, what False means" |

---

## Related Prompts

- [prompts/generation/generate-function.md](../generation/generate-function.md) — Generate the function before writing its docstring
- [prompts/review/code-review.md](../review/code-review.md) — Review documentation quality as a separate scope
