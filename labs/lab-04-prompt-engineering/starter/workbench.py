"""
Lab 04 — Prompt Engineering Workshop
Starter file: workbench.py

Each function in this file has an intentional gap designed to exercise
a specific prompt scenario from Module 04.

Do not fix these functions manually. Use Copilot with structured prompts.
See labs/lab-04-prompt-engineering/README.md for task instructions.
"""

import hashlib
import tomllib


# --- Scenario 1: Code Generation ---
# Gap: no type annotations, no file-existence validation, no error handling.
# Task: Write a generation prompt that adds validation and proper typing.

def parse_config(path):
    with open(path, "rb") as f:
        return tomllib.load(f)


# --- Scenario 2: Refactoring ---
# Gap: rate lookup logic is mixed into the calculation.
# Task: Write a refactoring prompt that extracts _get_tax_rate as a separate function.

def calculate_tax(amount, rate_key):
    rates = {
        "standard": 0.20,
        "reduced": 0.05,
        "zero": 0.00,
    }
    rate = rates.get(rate_key, 0.20)
    return round(amount * rate, 2)


# --- Scenario 3: Debugging ---
# Gap: off-by-one — the last element of the longer list is skipped.
# Task: Write a two-prompt chain: diagnose first, fix second.

def merge_sorted(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    # Bug: only one of the tails is handled; the other is silently dropped
    while i < len(a) - 1:
        result.append(a[i])
        i += 1
    while j < len(b) - 1:
        result.append(b[j])
        j += 1
    return result


# --- Scenario 4: Testing ---
# Gap: no tests exist for this function.
# Task: Write a testing prompt that produces a pytest suite with at least 4 cases.

DISCOUNT_CODES = {
    "SAVE10": 0.10,
    "HALF": 0.50,
}

def apply_discount(price, code):
    discount = DISCOUNT_CODES.get(code, 0.0)
    return round(price * (1 - discount), 2)


# --- Scenario 5: Documentation ---
# Gap: no docstring.
# Task: Write a documentation prompt for a Google-style docstring.

def validate_email(address):
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


# --- Scenario 6: Code Review ---
# Gap: no OWASP A01 review has been performed.
# Task: Write two review prompts — one for logic errors, one for OWASP A01.

def check_permissions(user, resource):
    if user.get("role") == "admin":
        return True
    allowed = resource.get("allowed_users", [])
    if user.get("id") in allowed:
        return True
    if resource.get("public"):
        return True
    return False


# --- Scenario 7: Security Review ---
# Gap: MD5 is cryptographically broken — OWASP A02:2021 violation.
# Task: Write a security review prompt anchored to OWASP A02.
# ⚠️  Premium model recommended for this task (o1 or Claude).

def hash_password(plaintext):
    return hashlib.md5(plaintext.encode()).hexdigest()
