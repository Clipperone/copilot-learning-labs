# Module 05 — Completion Checklist

Use this checklist after finishing the module and before starting Lab 05. If you cannot check an item confidently, revisit the linked section in [README.md](./README.md).

---

## Instruction Scopes

- [ ] I can name the 3 instruction scopes and state one use case for each: global, repository-wide, path-specific.
- [ ] I know which file path is required for repository-wide instructions: `.github/copilot-instructions.md`.
- [ ] I know the frontmatter key and format required for path-specific instructions: `applyTo` with a quoted glob.
- [ ] I can state the conflict resolution rule: narrower scope wins.

## The 4 Design Principles

- [ ] I can name all 4 principles: specific, imperative, bounded, non-contradictory.
- [ ] I can rewrite a vague instruction as a specific one by naming an explicit metric or list.
- [ ] I can rewrite a passive instruction ("it is preferred that...") as an imperative one.
- [ ] I know the completeness test: read it aloud — does it tell Copilot exactly what to produce?

## The 5 Instruction Domains

- [ ] I can write at least one instruction statement for each domain: coding style, architecture, testing, security, documentation.
- [ ] I know the domain template: `[DOMAIN]: [IMPERATIVE STATEMENT]. [EXPLICIT EXCEPTION IF ANY].`

## Path-Specific Instructions

- [ ] I can write a correct `applyTo` frontmatter block.
- [ ] I know the difference between `**` (recursive) and `*` (single directory level) in glob patterns.
- [ ] I know not to replicate repository-wide rules in path-specific files.

## Testing and Maintenance

- [ ] I know the diagnostic prompt pattern and how to use it to verify instructions are active.
- [ ] I can name 3 signs that an instruction file is being ignored: wrong path, file too long, passive language.
- [ ] I know to add a `Verified: YYYY-MM` comment at the top of every instruction file.
- [ ] I know the 4 audit triggers: dependency update, convention change, security fix, codebase restructure.

## Common Mistakes

- [ ] I know why one-off task instructions do not belong in instruction files.
- [ ] I know why instruction files exceeding ~400 words prose are silently ignored.
- [ ] I know why credentials must never appear in instruction files.

---

## Ready for Lab 05?

All items above checked → proceed to [Lab 05 — Write Your Project's Custom Instructions](../../labs/lab-05-custom-instructions/).

Not all items checked → return to [exercises.md](./exercises.md) for the specific principle you want to reinforce.
