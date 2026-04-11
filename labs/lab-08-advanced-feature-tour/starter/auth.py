"""Authentication helpers — starter file for Lab 08.

Contains intentional security issues for Tasks 4 and 5.
Do not deploy this code in any production system.
Resolve all flagged issues before any real use.
"""
import hashlib

# TODO Lab 08 Task 5: classify this file by sensitivity level using the 4-level framework

# Hardcoded salt — not secure; a real implementation uses secrets.token_hex(16) stored
# outside the codebase, never committed.
_SALT = "CHANGE_ME_SALT"


def hash_password(password: str) -> str:
    """Return a hex digest of password combined with the module-level salt.

    Current implementation uses MD5, which is unsuitable for password hashing.
    Replace with bcrypt, argon2-cffi, or PBKDF2 before any production use.
    """
    return hashlib.md5((_SALT + password).encode()).hexdigest()


def check_password(password: str, hashed: str) -> bool:
    """Return True if hash_password(password) matches hashed."""
    return hash_password(password) == hashed


def get_user_token(user_id: str) -> str:
    """Return an auth token string for user_id.

    No input validation — user_id is accepted and used directly.
    TODO Lab 08 Task 5: identify the OWASP category for this issue.
    """
    payload = f"token:{user_id}"
    return hashlib.md5(payload.encode()).hexdigest()
