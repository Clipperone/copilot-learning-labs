<!--
  Verified: 2026-04
  Update this date whenever you make a material change.
-->

# Project Instructions

## Coding Style

Use snake_case for all identifiers. Use type annotations on all function parameters and return values. Maximum line length: 100 characters.

## Architecture

Do not call data access logic directly from route handlers. All data access goes through the model layer. Route handlers receive validated input and return typed models — nothing else.

## Testing

Use pytest. Write one test function per case. Use bare assert statements — no unittest.TestCase. Include test cases for: null input, empty input, minimum value, maximum value. Name test functions after the behaviour under test: `test_<function>_<condition>_<expected>`.

## Security

Do not use MD5 or SHA1 for password hashing. Use `hashlib.pbkdf2_hmac` with a random salt. Flag OWASP A02:2021 (Cryptographic Failures) and OWASP A03:2021 (Injection) risks in any generated authentication or data-processing code.

## Documentation

Write Google-style docstrings with Args, Returns, and Raises sections on every public function. Audience: the caller, not the maintainer. Do not include usage examples unless the function has non-obvious behaviour.
