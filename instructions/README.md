# Custom Instruction Examples

Working examples of instruction files at each scope. Copy and adapt these for your own projects.

See [Module 05 — Instruction Scopes](../modules/05-custom-instructions/README.md#instruction-scopes) for the full explanation of when to use each scope.

---

| File | Scope | Description |
|------|-------|-------------|
| [global-example.md](./global-example.md) | User (global) | Personal habits applied across every project — naming preferences, documentation format, review checklist |
| [project-example.md](./project-example.md) | Repository-wide | Team conventions for a single project — architecture rules, testing framework, security defaults |
| [api-layer-example.md](./api-layer-example.md) | Path-specific | Tighter contract for one layer — `applyTo` frontmatter restricts the file to `src/api/**` only |

---

Copy any file and place it at the correct path for its scope:

| Scope | Path |
|-------|------|
| User (global) | VS Code Settings → Copilot → Instructions (UI) or `settings.json` |
| Repository-wide | `.github/copilot-instructions.md` |
| Path-specific | `.github/instructions/[name].instructions.md` with `applyTo` frontmatter |
