# Prompt Library

A curated collection of reusable, tested prompts for common coding scenarios.

## Categories

| Category | Focus | Prompts |
|----------|-------|---------|
| [generation/](./generation/) | Writing new code from a specification | Function, class, API endpoint |
| [debugging/](./debugging/) | Diagnosing and fixing problems | Symptom-based debug, explain error |
| refactoring/ | Improving structure without changing behavior | *(coming in v0.3)* |
| [testing/](./testing/) | Writing tests for existing code | [write-tests.md](./testing/write-tests.md) |
| [documentation/](./documentation/) | Writing and improving docs | [write-docstring.md](./documentation/write-docstring.md) |
| [review/](./review/) | Reviewing code for quality, style, and correctness | [code-review.md](./review/code-review.md) |
| [security/](./security/) | Identifying vulnerabilities and applying fixes | [security-audit.md](./security/security-audit.md) |
| [migration/](./migration/) | Migrating API call sites incrementally | [migrate-api.md](./migration/migrate-api.md) |

## How to Use a Prompt

1. Find the prompt that matches your task.
2. Copy it and fill in the `[UPPERCASE]` placeholders with your values.
3. Paste it into the Copilot chat panel in the appropriate mode (listed in the prompt file).
4. If results are poor, try the tips and failure notes at the bottom of each prompt file.

## How to Add a Prompt

Follow [templates/prompt-template.md](../templates/prompt-template.md) and open a PR.
Verify that the prompt produces correct output before submitting.

## Premium Request Guidance

All prompts are marked with whether a premium model is recommended.
`Premium model recommended: no` means the default model handles this well.
Only use a premium model when the task involves complex reasoning, multi-step logic, or security analysis.
