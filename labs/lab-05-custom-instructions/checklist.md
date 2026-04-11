# Lab 05 — Completion Checklist

Use this checklist after completing all four tasks. Each item maps to a specific task in [README.md](./README.md).

---

## Task 1 — Scope Analysis

- [ ] I classified all six constraints by scope (global / repo-wide / path-specific).
- [ ] I identified which constraints belong in the path-specific file because they apply only to the API layer.
- [ ] I confirmed that personal preferences (naming convention, verbosity) belong at global scope, not repo-wide.
- [ ] I checked my answers against [solution/README.md](./solution/README.md) after completing my own classification.

---

## Task 2 — Repository-Wide Instruction File

- [ ] I created the file at the exact path: `starter/.github/copilot-instructions.md`.
- [ ] The file starts with a Verified comment block that includes today's date.
- [ ] I wrote instruction statements covering at least four of the five domains: style, architecture, testing, security, documentation.
- [ ] Every statement passes the 4-principle check: specific, imperative, bounded, non-contradictory.
- [ ] The file is under 400 words of prose.

---

## Task 3 — Path-Specific Instruction File

- [ ] I created the file at `starter/.github/instructions/api-layer.instructions.md`.
- [ ] The file begins with a `---` frontmatter delimiter — no content before it.
- [ ] The frontmatter contains `applyTo: "src/api/**"`.
- [ ] The instructions in this file do not repeat or duplicate anything in the repo-wide file — they only add specificity.
- [ ] The file is under 200 words of prose.

---

## Task 4 — Verification

- [ ] I ran the diagnostic prompt in Ask mode exactly as written.
- [ ] The output applied at least one coding-style rule without being prompted (type annotations or snake_case).
- [ ] The output applied at least one documentation rule without being prompted (Google-style docstring).
- [ ] The output applied at least one API-specific rule without being prompted (typed return type or input validation).
- [ ] I identified and fixed any instruction that was not being applied (wrong path, file too long, passive language).
- [ ] I re-ran the diagnostic after fixing and confirmed that at least four rules now appear automatically.

---

## Common Mistakes Summary

- [ ] I did not use passive language ("it is preferred that...", "try to...", "ideally...") in any instruction statement.
- [ ] I did not write more than 400 words of prose in the repo-wide instruction file.
- [ ] I checked for contradictions between my global, repo-wide, and path-specific files.

---

## Completed?

All items above checked → proceed to [Module 06 — Agents and Role Specialization](../../modules/06-agents/).
