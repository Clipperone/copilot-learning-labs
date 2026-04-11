# Prompt: Security — OWASP-Anchored Security Audit

> **Category:** security
> **Difficulty:** advanced
> **Works best with:** ask mode
> **Premium model recommended:** yes
> **Verified:** 2026-04

---

## Purpose

Audit a single function for a specific OWASP Top 10 vulnerability category. Produces an exploit path before a fix — so you confirm the risk is real before acting on it.

---

## When to Use

- A function handles authentication, cryptography, access control, or untrusted input.
- You want to understand how a vulnerability could be exploited before deciding whether to fix it.
- You are working through a security checklist before a code review or release.

**Do not use when:** you want a general code quality review. This prompt is for security analysis only. Use the code review prompt for logic errors and style.

---

## The Prompt

```
Role: Act as a security engineer specializing in [LANGUAGE]/[FRAMEWORK].
Task: Audit `[FUNCTION_NAME]` for vulnerabilities matching [OWASP_CATEGORY].
Context: [LANGUAGE] [LANGUAGE_VERSION] · [FRAMEWORK] [FRAMEWORK_VERSION] · [ANY RELEVANT LIBRARY]
Constraints: Describe the exploit path before proposing any fix. Limit scope to [OWASP_CATEGORY]. Do not comment on naming, style, or concerns outside the stated OWASP category.
Output: Finding · exploit path · recommended fix · one-line code example of the fix.
```

---

## Example Usage

### Input context

```python
import hashlib

def hash_password(plaintext: str) -> str:
    return hashlib.md5(plaintext.encode()).hexdigest()
```

### Prompt (filled in)

```
Role: Act as a security engineer specializing in Python/standard library.
Task: Audit `hash_password` for vulnerabilities matching OWASP A02:2021 — Cryptographic Failures.
Context: Python 3.11 · standard library only · no external auth library
Constraints: Describe the exploit path before proposing any fix. Limit scope to OWASP A02. Do not comment on naming, style, or concerns outside cryptographic failures.
Output: Finding · exploit path · recommended fix · one-line code example of the fix.
```

### Expected output

```
Finding: `hash_password` uses MD5, which is not a password hashing algorithm.

Exploit path: An attacker who obtains the database can run a rainbow-table or dictionary
attack against MD5 hashes in seconds. MD5 has no salt and no iteration count, so the
cost to reverse a hash is near zero with commodity hardware.

Recommended fix: Replace MD5 with a password hashing function designed for the task:
PBKDF2-HMAC-SHA256 (standard library), bcrypt (third-party), or Argon2 (third-party).
Use a random per-password salt and a minimum of 600,000 iterations for PBKDF2.

Code example:
import hashlib, os
salt = os.urandom(16)
dk = hashlib.pbkdf2_hmac("sha256", plaintext.encode(), salt, 600_000)
```

---

## Variables to Customize

| Placeholder | What to put here | Example |
|-------------|-----------------|---------|
| `[FUNCTION_NAME]` | The function to audit | `hash_password` |
| `[OWASP_CATEGORY]` | The full OWASP category name and code | `OWASP A02:2021 — Cryptographic Failures` |
| `[LANGUAGE]` | Programming language | `Python` |
| `[LANGUAGE_VERSION]` | Runtime version | `3.11` |
| `[FRAMEWORK]` | Framework in use, or "standard library only" | `Django 4.2` |
| `[FRAMEWORK_VERSION]` | Framework version | `4.2` |

**Common OWASP categories for this prompt:**
- `A01:2021 — Broken Access Control`
- `A02:2021 — Cryptographic Failures`
- `A03:2021 — Injection`
- `A07:2021 — Identification and Authentication Failures`

---

## Tips

- Use a premium model (o1 or Claude) for this prompt. Exploit-path reasoning benefits from deeper multi-step analysis.
- Audit one function per prompt. Expanding scope beyond a single function dilutes the analysis.
- After receiving the audit, verify the exploit path by searching for published CVEs or exploit patterns for the specific algorithm or pattern named.
- Before accepting the fix, write the OWASP risk name in a comment on the line above the corrected call — so reviewers know why the change was made.

## Common Failures

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Output is generic security advice not tied to the code | No function scoped, no OWASP category | Name the specific function and OWASP category in the Task line |
| Fix is proposed before exploit path | "Describe exploit path before fix" constraint missing | Add the constraint explicitly |
| Language/version context ignored | Context line absent | Add the Context line with exact runtime version |
| Output references CVEs for a different language | Framework not specified | Add framework name and version to the Context line |

---

## Related Prompts

- [prompts/review/code-review.md](../review/code-review.md) — Scoped code review for logic and style before security audit
- [prompts/generation/generate-function.md](../generation/generate-function.md) — Generate a replacement function after confirming the fix
