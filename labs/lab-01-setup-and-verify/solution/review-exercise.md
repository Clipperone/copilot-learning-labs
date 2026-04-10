# Critical Review Exercise — Reference Solution

---

## Snippet A

```python
import csv

def read_active_users(filepath: str) -> list[dict]:
    results = []
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["status"] == "active":
                results.append(row)
    return results
```

**Read — Did you read every line before answering?**

Yes. The function opens a CSV file, iterates over rows using `csv.DictReader`, filters rows where the `status` field equals `"active"`, appends matching rows to `results`, and returns the list.

**Run — Does this code execute without errors given a valid CSV file with a 'status' column?**

Yes, with a valid file and a `status` column present it runs correctly. However, if the file does not exist, `open()` raises `FileNotFoundError`. If the CSV has no `status` column, `row["status"]` raises a `KeyError`. Neither case is handled.

**Reason — Does it do exactly what was asked? Are there side effects or edge cases?**

It does what was asked for the happy path. Edge cases not handled: missing file, missing column, empty CSV, non-string values in `status`, and encoding issues with non-ASCII content. The function also loads all matching rows into memory — a problem for very large files.

**Risk — Does it introduce any security or correctness concern?**

Low risk for typical internal use. No user input flows into the file path here, so OWASP A03 (injection) is not triggered. However, if `filepath` were ever derived from user input without validation, path traversal (OWASP A01) would be a concern. The missing error handling is a correctness risk, not a security risk.

---

## Snippet B

```python
import hashlib

def store_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()
```

**Read — Did you read every line before answering?**

Yes. The function takes a plaintext password string, encodes it to bytes, hashes it with MD5, and returns the hex digest.

**Run — Does this code execute without errors?**

Yes. It runs without errors and returns a 32-character hex string.

**Reason — Does it do what a password storage function is supposed to do?**

No. A secure password storage function must use a slow, salted, purpose-built password hashing algorithm. MD5 is a fast, general-purpose hash with no salt — it is cryptographically broken for this use case.

**Risk — Does it introduce any security concern? Be specific.**

Critical risk. MD5 is not a password hashing algorithm. It is:

1. **Fast** — attackers can test billions of MD5 hashes per second using GPUs.
2. **Unsalted** — two users with the same password produce the same hash; rainbow table attacks trivially reverse common passwords.
3. **Cryptographically broken** — collision vulnerabilities are well-documented.

This is an OWASP A02 (Cryptographic Failures) violation. AI generated this pattern because it is common in older tutorials — it is plausible text but critically incorrect for password storage.

---

## Final Question

**Snippet B** contains the dangerous flaw. The MD5 hash is not a password hashing algorithm — it is fast, unsalted, and broken for this purpose, making stored passwords trivially reversible.

**Correct alternative:** Use `bcrypt`, `argon2`, or Python's `hashlib.scrypt` (with a salt). In Python, the `bcrypt` library or `passlib` are the standard choices:

```python
import bcrypt

def store_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```
