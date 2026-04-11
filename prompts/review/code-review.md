# Prompt: Review — Scoped Code Review

> **Category:** review
> **Difficulty:** intermediate
> **Works best with:** ask mode
> **Premium model recommended:** no
> **Verified:** 2026-04

---

## Purpose

Review a single function for one specific concern — logic errors, OWASP A01 access control, style, or test coverage — and receive actionable, numbered findings.

---

## When to Use

- Before merging a function that handles critical logic or authorization.
- When you want a logic pass separate from a security pass.
- When a reviewer has found issues and you want Copilot to enumerate similar concerns systematically.

**Do not use when:** you want a whole-file review. Scope to one function or one concern at a time. Whole-file reviews produce unactionable walls of notes.

---

## The Prompt

```
Task: Review `[FUNCTION_NAME]` for [REVIEW_SCOPE].
Constraints: Focus only on [REVIEW_SCOPE]. Do not comment on naming, formatting, or anything outside [REVIEW_SCOPE].
Output: A numbered list — each item: finding · severity (high / medium / low) · one-sentence suggested fix.
```

---

## Example Usage

### Input context

```python
def check_permissions(user: dict, resource: dict) -> bool:
    if user.get("role") == "admin":
        return True
    allowed = resource.get("allowed_users", [])
    if user.get("id") in allowed:
        return True
    if resource.get("public"):
        return True
    return False
```

### Prompt (filled in)

```
Task: Review `check_permissions` for OWASP A01:2021 — Broken Access Control.
Constraints: Focus only on OWASP A01. Do not comment on naming, formatting, or anything outside access control.
Output: A numbered list — each item: finding · severity (high / medium / low) · one-sentence suggested fix.
```

### Expected output

```
1. Finding: The `resource` dict is accepted as caller-supplied input with no ownership verification.
   Severity: High
   Fix: Retrieve the resource from a trusted data layer using only a resource ID from the caller — never accept a full resource dict as input.

2. Finding: No rate limiting or logging of denied access attempts.
   Severity: Medium
   Fix: Log denied access with user ID and resource ID for audit trail and abuse detection.
```

---

## Variables to Customize

| Placeholder | What to put here | Example |
|-------------|-----------------|---------|
| `[FUNCTION_NAME]` | The function to review | `check_permissions` |
| `[REVIEW_SCOPE]` | The specific concern to review | `OWASP A01:2021 — Broken Access Control` |

**Common values for `[REVIEW_SCOPE]`:**
- `logic errors` — any condition that grants or denies incorrectly
- `OWASP A01:2021 — Broken Access Control`
- `OWASP A03:2021 — Injection`
- `style — PEP 8 compliance`
- `test coverage — uncovered paths`

---

## Tips

- Always run two separate review prompts for logic and security. Combining them produces mixed severity ratings that are hard to triage.
- After receiving findings, ask a follow-up: "Which of these findings applies to the current code as written, not hypothetically?" to filter speculative notes.
- Use `ask mode` for review prompts — you want analysis, not inline edits.

## Common Failures

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Findings are generic security advice, not tied to the code | Scope too broad | Name the specific OWASP category and the specific function |
| Findings include naming and style notes | Missing "do not comment on" constraint | Add explicit exclusions to the Constraints line |
| Severity ratings are inconsistent | Copilot's default rubric varies | Add "Use this severity scale: high = exploitable / medium = design risk / low = style" |

---

## Related Prompts

- [prompts/security/security-audit.md](../security/security-audit.md) — Deep security review with exploit path
- [prompts/testing/write-tests.md](../testing/write-tests.md) — Write tests after identifying uncovered paths
