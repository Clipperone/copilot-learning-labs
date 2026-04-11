# Prompt: Migration — Migrate a Single API Call Site

> **Category:** migration
> **Difficulty:** advanced
> **Works best with:** ask mode | inline chat
> **Premium model recommended:** no
> **Verified:** 2026-04

---

## Purpose

Migrate one call site from a source API to a target API, preserving the original behavior, error handling contract, and return type. Chain multiple instances of this prompt to migrate an entire module incrementally.

---

## When to Use

- You are migrating from one library version to another (e.g., `requests` → `httpx`, `boto3 v1` → `boto3 v2`).
- You want to migrate one call site at a time and verify each one before continuing.
- You need to preserve error handling or specific return semantics across the migration.

**Do not use when:** you want to migrate an entire file in one prompt. Large migrations are unreliable as single prompts — chain this prompt per call site instead.

---

## The Prompt

```
Task: Rewrite the call to `[OLD_API_METHOD]` at [FILE_PATH]:[LINE_NUMBER] to use `[NEW_API_METHOD]` from `[TARGET_LIBRARY]`.
Context: Source API: [SOURCE_LIBRARY] [SOURCE_VERSION] · Target API: [TARGET_LIBRARY] [TARGET_VERSION]
Constraints: Preserve the return type: [RETURN_TYPE]. Preserve error handling: [ERROR_HANDLING_DESCRIPTION]. Do not change any other lines.
Output: The updated line(s) only — no surrounding context.
```

---

## Example Usage

### Input context

```python
# File: services/http_client.py, line 14
import requests

def fetch_user(user_id: str) -> dict:
    response = requests.get(f"https://api.example.com/users/{user_id}", timeout=5)
    response.raise_for_status()
    return response.json()
```

### Prompt (filled in)

```
Task: Rewrite the call to `requests.get` at services/http_client.py:14 to use `httpx.get` from `httpx`.
Context: Source API: requests 2.31 · Target API: httpx 0.27
Constraints: Preserve the return type: dict (from .json()). Preserve error handling: raise_for_status() must remain. Do not change any other lines.
Output: The updated line(s) only — no surrounding context.
```

### Expected output

```python
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.example.com/users/{user_id}", timeout=5)
        response.raise_for_status()
        return response.json()
```

---

## Variables to Customize

| Placeholder | What to put here | Example |
|-------------|-----------------|---------|
| `[OLD_API_METHOD]` | The method being replaced | `requests.get` |
| `[FILE_PATH]` | Relative path to the file | `services/http_client.py` |
| `[LINE_NUMBER]` | Line number of the call site | `14` |
| `[NEW_API_METHOD]` | The replacement method | `httpx.AsyncClient.get` |
| `[TARGET_LIBRARY]` | The library being migrated to | `httpx` |
| `[SOURCE_LIBRARY]` | The library being migrated from | `requests 2.31` |
| `[TARGET_VERSION]` | Target library version | `0.27` |
| `[RETURN_TYPE]` | The return type to preserve | `dict` |
| `[ERROR_HANDLING_DESCRIPTION]` | How errors are currently handled | `raise_for_status() is called; callers expect `HTTPStatusError`` |

---

## Chaining This Prompt

For a full-file migration, run these three prompts in sequence:

1. **Discovery prompt:** "List every call site that uses `[OLD_API_METHOD]` in [FILE]. Output: line number · call expression, one per line."
2. **Migration prompt (this prompt):** Run once per call site from the discovery list.
3. **Verification prompt:** "Confirm that the rewritten call at [FILE]:[LINE] preserves [SPECIFIC_BEHAVIOR]. Output: yes or no with one sentence of justification."

---

## Tips

- Always run the discovery prompt first. Do not guess how many call sites exist.
- If the target API is async and the source is sync, state this explicitly in the Constraints line: "The calling function must also become async — include the function signature change."
- Specify the library versions. Copilot's training data may include multiple API versions, and an unversioned prompt can produce code for the wrong one.

## Common Failures

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Copilot migrates more than the specified line | Missing "do not change any other lines" constraint | Add the constraint; scope more tightly with the line number |
| Return type changes unexpectedly | Return type not specified | Add explicit return type to the Constraints line |
| Error handling is removed silently | No error handling constraint | Describe the existing error contract in the Constraints line |
| Output is for the wrong library version | Version not specified | Add source and target version to the Context line |

---

## Related Prompts

- [prompts/review/code-review.md](../review/code-review.md) — Review the migrated call site for correctness
- [prompts/debugging/debug-from-symptoms.md](../debugging/debug-from-symptoms.md) — Debug migration-related failures after the rewrite
