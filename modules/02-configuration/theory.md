# Module 02: Configuration — Extended Theory

> Reference material to supplement the module README. Read this for deeper context or when the README summary is insufficient.

---

## Settings Precedence in VS Code

VS Code applies settings in a defined merge order. Later entries override earlier ones for the same key:

1. **Default VS Code settings** — built-in defaults
2. **User settings** — `%APPDATA%\Code\User\settings.json` (Windows) / `~/.vscode/settings.json` (Linux/macOS)
3. **Workspace settings** — `.vscode/settings.json` in the project root
4. **Folder settings** — in multi-root workspaces, folder-level settings override workspace settings

For team projects, commit `.vscode/settings.json` to the repository. Do not commit user-level settings — they belong to the individual.

---

## Copilot Settings Reference

Relevant settings for professional Copilot configuration:

| Setting | Type | Default | Recommended | Purpose |
|---------|------|---------|-------------|---------|
| `github.copilot.enable` | Object | `{"*": true}` | `{"*": true}` | Enable/disable per language |
| `github.copilot.editor.enableAutoCompletions` | Boolean | `true` | `true` | Show ghost text as you type |
| `github.copilot.chat.codeGeneration.useInstructionFiles` | Boolean | `false` | `true` | Apply `.github/copilot-instructions.md` |
| `github.copilot.chat.followUps` | String | `"always"` | `"always"` | Show follow-up question suggestions |
| `github.copilot.renameSuggestions.triggerAutomatically` | Boolean | `true` | `true` | Suggest renames on symbol rename |
| `editor.inlineSuggest.enabled` | Boolean | `true` | `true` | Required for ghost text to appear |

To disable Copilot for a specific language (e.g., plaintext):

```json
"github.copilot.enable": {
  "*": true,
  "plaintext": false,
  "markdown": true
}
```

---

## `.github/copilot-instructions.md` — Deep Reference

### How instructions are applied

Instructions in `.github/copilot-instructions.md` are injected into the system prompt of every Copilot chat session (Ask, Edit, Plan, Agent) when `useInstructionFiles` is `true`. They are **not** applied to inline completions.

Instructions are applied in addition to Copilot's built-in behavior — they extend it, they do not replace it. Copilot will not violate safety rules or generate clearly harmful code regardless of instructions.

### Effective instruction patterns

| Pattern | Example | Effect |
|---------|---------|--------|
| Language constraint | "All code is Python 3.12. Do not suggest `asyncio` unless I ask." | Reduces off-target completions |
| Naming convention | "Use `snake_case` for functions and variables. Use `PascalCase` for classes." | Style consistency |
| Error handling policy | "Always raise specific exceptions; never use bare `except:` clauses." | Reduces error-prone patterns |
| Test framework | "Tests use `pytest`. Do not suggest `unittest`." | Framework alignment |
| Security rule | "Never generate SQL by string concatenation. Use parameterized queries only." | OWASP A03 prevention |
| Negative scope | "Do not suggest code outside the `src/` folder unless explicitly asked." | Focus boundaries |

### What instructions cannot do

- Override Copilot's content safety filters
- Give Copilot access to files it cannot see
- Guarantee compliance on every response (LLMs are probabilistic)
- Replace code review and security testing

### Instruction file hygiene

- **Keep instructions under 1000 characters per rule block.** Longer blocks reduce compliance.
- **One instruction per bullet.** Compound bullets ("do X and also Y") are less reliable.
- **Remove instructions that no longer apply.** Stale rules create contradictions.
- **Test instructions by asking: "What are your coding conventions for this project?"** — Copilot will summarize what it has read.

---

## File Organization for AI-Assisted Projects

Copilot builds context from open tabs, referenced files, and the surrounding buffer. File organization directly affects suggestion quality.

### Recommended structure for a Python project

```
project/
├── .github/
│   └── copilot-instructions.md
├── .vscode/
│   ├── settings.json
│   ├── tasks.json
│   └── extensions.json
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── models.py       ← data models only
│       ├── services.py     ← business logic only
│       ├── repository.py   ← data access only
│       └── api.py          ← HTTP layer only
├── tests/
│   ├── test_models.py
│   ├── test_services.py
│   └── test_api.py
├── .editorconfig
├── pyproject.toml
└── README.md
```

Each file has a single responsibility. Copilot receives unambiguous context when editing `services.py` — it knows that file contains business logic, not database queries.

### Patterns that degrade AI context

| Anti-pattern | Problem | Better approach |
|-------------|---------|----------------|
| `utils.py` with 800 lines | Everything is in scope; context is ambiguous | Split into `validators.py`, `formatters.py`, `converters.py` |
| Commented-out code | Stale code confuses the model about what is active | Delete commented-out code; use git history instead |
| Magic numbers inline | `if status == 3:` — unclear to model and human | Use named constants: `if status == STATUS_ACTIVE:` |
| Deep nesting (5+ levels) | Model loses track of scope | Refactor to early returns or helper functions |
| Inconsistent naming | `getUserData`, `get_user_info`, `fetchUser` in same project | One naming convention, enforced by linter |

---

## Linting and Formatting Tools Reference

### Python

| Tool | Role | Config file |
|------|------|------------|
| [Ruff](https://docs.astral.sh/ruff/) | Lint + format (replaces Black + Flake8 in most cases) | `pyproject.toml` or `ruff.toml` |
| [Black](https://black.readthedocs.io/) | Opinionated formatter | `pyproject.toml` |
| [mypy](https://mypy.readthedocs.io/) | Static type checking | `mypy.ini` or `pyproject.toml` |
| [Bandit](https://bandit.readthedocs.io/) | Security lint | `bandit.yaml` |

Minimal `pyproject.toml` for Ruff:

```toml
[tool.ruff]
line-length = 120
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "S", "UP"]
```

### JavaScript / TypeScript

| Tool | Role | Config file |
|------|------|------------|
| [ESLint](https://eslint.org/) | Lint | `eslint.config.js` |
| [Prettier](https://prettier.io/) | Format | `.prettierrc` |
| [TypeScript](https://www.typescriptlang.org/) | Type checking | `tsconfig.json` |

---

## VS Code Tasks — Deep Reference

Tasks are defined in `.vscode/tasks.json`. They appear in **Terminal → Run Task** and are accessible from agent mode via the terminal tool.

A task with `"group": {"kind": "test", "isDefault": true}` becomes the default test task, runnable with `Ctrl+Shift+P → Tasks: Run Test Task`.

Task properties relevant to Copilot agent mode:
- `"type": "shell"` — runs a shell command; agent can capture output
- `"presentation": {"reveal": "always"}` — shows output in the terminal panel

---

## Official Resources

- [VS Code Settings reference](https://code.visualstudio.com/docs/getstarted/settings)
- [Copilot customization in VS Code](https://code.visualstudio.com/docs/copilot/copilot-customization)
- [copilot-instructions.md documentation](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)
- [EditorConfig specification](https://editorconfig.org/)
- [Ruff documentation](https://docs.astral.sh/ruff/)
