# Lab 05 — Solution Reference

This folder contains reference answers for Lab 05 tasks. Read these only **after** completing your own work.

---

## Task 1 — Scope Assignment Reference Answers

| # | Constraint | Correct scope | Reasoning |
|---|-----------|---------------|-----------|
| 1 | "All public functions must have Google-style docstrings." | **Repo-wide** | A project convention — applies to all contributors and all files in this repo. |
| 2 | "Do not use MD5 or SHA1 for password hashing." | **Repo-wide** | A security baseline that governs all code in the project, not just one layer. |
| 3 | "Do not return raw dicts from route handlers — use a typed model." | **Path-specific** (`src/api/**`) | This constraint is meaningful only for route handlers; applying it everywhere adds noise. |
| 4 | "I always prefer snake_case for identifiers." | **Global** | A personal preference that applies to all your projects on this machine — not a project-specific convention. |
| 5 | "Use pytest. One test function per case." | **Repo-wide** | A project's testing framework choice applies to all contributors; it is not personal and not layer-specific. |
| 6 | "Validate all request input at the route handler boundary." | **Path-specific** (`src/api/**`) | Validation at the boundary is an API-layer contract. Applying it everywhere would impose route-handler semantics on models, services, and utilities. |

---

## Solution Files in This Folder

| File | Where it should go in the starter project | Purpose |
|------|------------------------------------------|---------|
| `copilot-instructions.md` | `starter/.github/copilot-instructions.md` | Repository-wide instruction file |
| `api-layer.instructions.md` | `starter/.github/instructions/api-layer.instructions.md` | Path-specific instruction file for `src/api/**` |

Compare your files against these references. Focus on:

1. **Specificity** — are your statements as precise as the reference?
2. **Imperative verbs** — does every statement use an imperative verb (Use, Do not, Write, Flag)?
3. **Boundary conditions** — are limits stated explicitly (100 characters, 400 words, null/empty/boundary)?
4. **No duplication** — does the path-specific file only add constraints, not repeat repo-wide ones?
