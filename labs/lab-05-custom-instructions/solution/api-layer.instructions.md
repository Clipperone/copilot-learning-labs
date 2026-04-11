---
applyTo: "src/api/**"
---

<!--
  Verified: 2026-04
  Update this date whenever you make a material change.
-->

# API Layer Instructions

Security: Validate all request input at the route handler boundary before passing to the model layer. Flag OWASP A03:2021 (Injection) risks on any query or command construction.

Return types: Every route handler must return a TypedDict or dataclass — never a raw dict. Annotate the return type explicitly.

Error handling: All route handlers must catch exceptions and return structured error responses with a consistent shape. Never expose stack traces or internal error messages in HTTP responses.
