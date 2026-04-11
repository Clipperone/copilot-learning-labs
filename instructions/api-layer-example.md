---
applyTo: "src/api/**"
---

<!--
  Example: Path-specific instruction file
  Scope: Files matching src/api/**
  File location: .github/instructions/api-layer.instructions.md
  Verified: 2026-04

  Path-specific files add constraints that apply only to a single area of the codebase.
  Do not repeat instructions already in .github/copilot-instructions.md — add specificity only.
  The applyTo frontmatter must be the very first content in the file.
-->

# API Layer Instructions

Security: Validate all request input at the route handler boundary before passing to the service or model layer. Flag OWASP A03:2021 (Injection) on any query or command construction.

Return types: Every route handler must return a TypedDict or dataclass — never a raw dict. Annotate the return type explicitly on every handler.

Error handling: All route handlers must catch exceptions and return structured error responses with a consistent shape. Never expose stack traces or internal error messages in HTTP responses.
