# Starter Project

This is the working target for Lab 05 — Custom Instructions.

The project is intentionally sparse: no type annotations, no docstrings, no tests, and one security vulnerability. Your task is not to add these manually. Your task is to write instruction files that make Copilot add them automatically whenever it generates or modifies code in this project.

## Structure

```
src/
  api/
    users.py    ← route handlers (no types, no validation, no docstrings)
    auth.py     ← password hashing with MD5 (OWASP A02:2021 violation — intentional)
  models/
    user.py     ← User model (no type annotations)
tests/
  test_users.py ← empty test file
```

## What Your Instruction Files Should Fix

When your instruction files are complete and Copilot is reading them, any new function Copilot generates in this project should automatically include:

- Type annotations on parameters and return values
- A Google-style docstring
- Input validation at the API boundary
- A typed return model (not a raw dict) from route handlers
- No use of MD5 or SHA1

You verify this in Task 4 using the diagnostic prompt in the lab README.
