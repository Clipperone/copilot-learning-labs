# Prompt: Generate a Function from a Specification

> **Category:** generation
> **Difficulty:** basic
> **Works best with:** ask mode | agent mode
> **Premium model recommended:** no
> **Verified:** 2026-04

---

## Purpose

Generate a well-structured, readable function from a plain-language description. Use when you know what a function should do but want Copilot to produce the implementation.

---

## When to Use

- You have a clear specification for a function (inputs, outputs, constraints)
- You want a first draft that you will review and refine
- You are writing boilerplate or standard utility logic

**Do not use when:** the function is part of a larger refactoring; use the refactoring prompts instead. Do not use when you need architecture guidance; use Plan mode.

---

## The Prompt

```
Write a [LANGUAGE] function named [FUNCTION_NAME] that [DESCRIPTION].

Inputs: [INPUT_PARAMS] — [TYPES_AND_DESCRIPTIONS]
Output: [RETURN_VALUE] — [TYPE_AND_DESCRIPTION]
Constraints: [CONSTRAINTS — e.g., "must handle null input", "must not mutate the input list", "must be O(n)"]

Requirements:
- [REQUIREMENT_1]
- [REQUIREMENT_2]

Do not use external libraries unless I specify them.
Return only the function — no test code, no usage example, no wrapper class.
```

---

## Example Usage

### Input context

*(no prior code needed — this is a greenfield function)*

### Prompt (filled in)

```
Write a Python function named parse_duration that converts a duration string like "2h 30m" into total seconds.

Inputs: duration_str (str) — a human-readable duration string with hours (h), minutes (m), and/or seconds (s) components
Output: int — total number of seconds represented by the input string

Constraints:
- must handle inputs that contain only some components (e.g., "45m", "1h 10s")
- must raise ValueError for unrecognized formats
- must not use external libraries

Requirements:
- Use regex to parse the string
- Zero-pad is not required

Do not use external libraries unless I specify them.
Return only the function — no test code, no usage example, no wrapper class.
```

### Expected output

```python
import re

def parse_duration(duration_str: str) -> int:
    pattern = re.compile(r'(?:(\d+)h)?\s*(?:(\d+)m)?\s*(?:(\d+)s)?')
    match = pattern.fullmatch(duration_str.strip())
    if not match or not any(match.groups()):
        raise ValueError(f"Unrecognized duration format: '{duration_str}'")
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    return hours * 3600 + minutes * 60 + seconds
```

---

## Variables to Customize

| Placeholder | What to put here | Example |
|-------------|-----------------|---------|
| `[LANGUAGE]` | Programming language | `Python` |
| `[FUNCTION_NAME]` | Exact function name | `parse_duration` |
| `[DESCRIPTION]` | What the function does | `converts a duration string into total seconds` |
| `[INPUT_PARAMS]` | Parameter names and types | `duration_str (str)` |
| `[RETURN_VALUE]` | Return type and meaning | `int — total seconds` |
| `[CONSTRAINTS]` | Must/must not rules | `must raise ValueError for bad input` |

---

## Tips

- More specific constraints produce more correct and safer code.
- Specifying `"Return only the function"` avoids wasted tokens on scaffolding you don't need.
- If the output includes unnecessary imports or boilerplate, add: `Do not include import statements.`

## Common Failures

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Output includes a test or `main()` block | Constraints not specific enough | Add: `Return only the function — no test code` |
| Uses an external library you didn't want | Copilot assumes convenience is preferred | Add: `Do not use external libraries` |
| Output is overly verbose | No output format constraint | Add: `Be concise — avoid unnecessary comments` |

---

## Related Prompts

- [generate-class.md](./generate-class.md) — when the function belongs in a class
- [debugging/explain-error.md](../debugging/explain-error.md) — when the generated function fails
