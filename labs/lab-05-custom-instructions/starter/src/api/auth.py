import hashlib


# WARNING: This file intentionally contains a security vulnerability (OWASP A02:2021).
# It is provided as a teaching artifact for Lab 05, Task 4 — Security instruction verification.
# Do not use this code in production.

def hash_password(plaintext):
    return hashlib.md5(plaintext.encode()).hexdigest()


def check_password(plaintext, hashed):
    return hash_password(plaintext) == hashed
