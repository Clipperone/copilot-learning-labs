# Templates

This folder contains reusable templates for all content types in the course repository.

## Available Templates

| Template | Purpose | Used for |
|----------|---------|---------|
| [module-readme-template.md](./module-readme-template.md) | Standard structure for module README files | `/modules/XX-*/README.md` |
| [lab-readme-template.md](./lab-readme-template.md) | Standard structure for lab README files | `/labs/lab-XX-*/README.md` |
| [prompt-template.md](./prompt-template.md) | Standard structure for prompt library entries | `/prompts/**/*.md` |
| [agent-definition-template.md](./agent-definition-template.md) | Standard structure for agent persona definitions | `/agents/*.md` |

## Usage

When creating a new module, lab, prompt, or agent definition:

1. Copy the relevant template.
2. Replace all `[PLACEHOLDER]` values.
3. Delete comment blocks (`<!-- -->`).
4. Verify against the completion criteria section.

## Contributing

If you improve a template, open a PR and explain the rationale. A template change affects all future content, so include a migration note in the PR description.
