<!--
  Example: Repository-wide instruction file
  Scope: All Copilot sessions in this repository
  File location: .github/copilot-instructions.md
  Verified: 2026-04

  Repository-wide instructions encode conventions that every contributor must follow.
  Keep this file under 400 words of prose. Split into path-specific files when a layer
  needs a tighter contract than the project default.
-->

# Project Instructions

## Coding Style

Use snake_case for all identifiers. Use type annotations on all function parameters and return values. Maximum line length: 100 characters.

## Architecture

Do not call the data access layer directly from route handlers. All data access goes through the repository layer. Route handlers receive validated input — they do not perform business logic or data formatting.

## Testing

Use pytest. Write one test function per case. Use bare assert statements — no unittest.TestCase. Cover null input, empty input, and boundary values in every test suite. Name test functions after the behaviour under test: `test_<function>_<condition>_<expected>`.

## Security

Do not use MD5 or SHA1 for password hashing. Use `hashlib.pbkdf2_hmac` with a random salt. Flag OWASP A02:2021 (Cryptographic Failures) and OWASP A03:2021 (Injection) risks in any generated authentication or data-processing code.

## Documentation

Write Google-style docstrings with Args, Returns, and Raises sections on every public function. Audience: the caller, not the maintainer. Do not include usage examples unless the function has non-obvious behaviour.
