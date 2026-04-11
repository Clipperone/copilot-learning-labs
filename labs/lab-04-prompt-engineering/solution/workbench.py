"""
Lab 04 — Prompt Engineering Workshop
Solution file: workbench.py

Each function below shows one valid implementation of the task described
in labs/lab-04-prompt-engineering/README.md.

Your implementation may differ — what matters is that the success criteria
in the lab README are met, not that your code matches this file exactly.
"""

import hashlib
import os
import pathlib
import tomllib


# --- Scenario 1: Code Generation ---
# Validated, typed, with FileNotFoundError on missing path.

def parse_config(path: str | pathlib.Path) -> dict:
    resolved = pathlib.Path(path)
    if not resolved.exists():
        raise FileNotFoundError(f"Config file not found: {resolved}")
    with resolved.open("rb") as f:
        return tomllib.load(f)


# --- Scenario 2: Refactoring ---
# Rate lookup extracted into a private helper; public interface unchanged.

_TAX_RATES: dict[str, float] = {
    "standard": 0.20,
    "reduced": 0.05,
    "zero": 0.00,
}


def _get_tax_rate(rate_key: str) -> float:
    return _TAX_RATES.get(rate_key, 0.20)


def calculate_tax(amount: float, rate_key: str) -> float:
    rate = _get_tax_rate(rate_key)
    return round(amount * rate, 2)


# --- Scenario 3: Debugging ---
# Fixed: both tails are now fully appended using slice extension.

def merge_sorted(a: list, b: list) -> list:
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


# --- Scenario 4: Testing ---
# Reference — see starter/test_apply_discount.py for the full pytest suite.

DISCOUNT_CODES = {
    "SAVE10": 0.10,
    "HALF": 0.50,
}


def apply_discount(price: float, code: str) -> float:
    discount = DISCOUNT_CODES.get(code, 0.0)
    return round(price * (1 - discount), 2)


# --- Scenario 5: Documentation ---

def validate_email(address: str) -> bool:
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
# Logic is sound for the defined contract; an OWASP A01 reviewer would flag
# the missing resource ownership check if users can supply their own `resource`
# dictionaries. Noted here for reference — not fixed in the solution because
# the fix depends on the application's data layer.

def check_permissions(user: dict, resource: dict) -> bool:
    if user.get("role") == "admin":
        return True
    allowed = resource.get("allowed_users", [])
    if user.get("id") in allowed:
        return True
    if resource.get("public"):
        return True
    return False


# --- Scenario 7: Security Review ---
# OWASP A02:2021 — Cryptographic Failures
# MD5 is not a password hashing algorithm. It has no salt, no iterations,
# and is trivially reversed with rainbow tables. Replaced with PBKDF2-HMAC-SHA256
# using a per-password salt and 600,000 iterations (OWASP recommended minimum 2023).

def hash_password(plaintext: str) -> str:
    salt = os.urandom(16)
    # OWASP A02:2021 — use PBKDF2-HMAC-SHA256 with salt and sufficient iterations
    dk = hashlib.pbkdf2_hmac("sha256", plaintext.encode(), salt, 600_000)
    return salt.hex() + ":" + dk.hex()
