# Contributing to copilot-learning-labs

Thank you for your interest in improving this course. All contributions — content fixes, new labs, improved prompts, updated examples, translation notes — are welcome.

---

## Ways to Contribute

| Type | Description |
|------|-------------|
| **Content fix** | Correct outdated information, broken links, or errors |
| **Clarification** | Improve explanations, add missing context |
| **New lab or exercise** | Add a new hands-on task following the lab template |
| **Prompt improvement** | Refine or add to the prompt library |
| **Agent definition** | Add or improve an agent persona |
| **Translation** | Translate a module or lab into another language |
| **Typo / formatting** | Fix spelling, grammar, or markdown formatting |

---

## Before You Start

1. **Search existing issues and PRs** — your idea may already be in progress.
2. **Open an issue first** for significant changes (new modules, restructuring, template changes). Use the appropriate [issue template](./.github/ISSUE_TEMPLATE/).
3. **For small fixes** (typos, broken links, outdated dates), a direct PR is fine — no issue needed.

---

## How to Contribute

### 1. Fork and clone

```bash
git clone https://github.com/YOUR_USERNAME/copilot-learning-labs.git
cd copilot-learning-labs
```

### 2. Create a branch

Use a descriptive branch name:

```bash
git checkout -b fix/module-01-typos
git checkout -b feat/lab-11-security-review
git checkout -b update/prompt-debugging-null-handling
```

### 3. Make your changes

Follow the conventions below and use the templates in [/templates](./templates/).

### 4. Open a pull request

Use the [PR template](./.github/PULL_REQUEST_TEMPLATE.md). Include:

- What changed and why
- Which module, lab, or asset is affected
- Whether any links or cross-references were updated

---

## Content Conventions

### Markdown

- Use ATX headings (`#`, `##`, `###`) — no underline style.
- Put one blank line before and after headings, lists, and code blocks.
- Wrap code samples in fenced code blocks with a language hint (` ```python `).
- Keep lines under 120 characters where practical.

### Modules

- Follow [templates/module-readme-template.md](./templates/module-readme-template.md) exactly.
- `theory.md` must stay under 500 words of core prose (tables and code blocks excluded).
- Always include the `Verified: YYYY-MM` date in the module header.
- Always include the `⚠️ Premium request note` callout.

### Labs

- Follow [templates/lab-readme-template.md](./templates/lab-readme-template.md) exactly.
- Include a `starter/` folder with any files the learner needs to begin.
- Include a `solution/` folder unless the lab is purely exploratory.
- Every lab must have a `checklist.md`.

### Prompts

- Follow [templates/prompt-template.md](./templates/prompt-template.md).
- Include at least one realistic example with actual input and expected output.
- State whether a premium model is recommended.

### Agents

- Follow [templates/agent-definition-template.md](./templates/agent-definition-template.md).
- Always define at least one handoff: who takes over and when.

---

## Feature Verification

If you update content that references a specific GitHub Copilot feature:

- Verify against the [official documentation](https://docs.github.com/en/copilot) before publishing.
- Update the `Verified: YYYY-MM` field in the module or file header.
- Note any plan-specific restrictions (Pro vs. Pro+ vs. Business vs. Enterprise).

---

## What Not to Do

- Do not add speculative features ("this will soon support…").
- Do not reproduce copyrighted third-party content.
- Do not commit secrets, credentials, or personal data — even in example files.
- Do not change the template structure without opening an issue first. Templates affect all future content.

---

## Community

- Use [GitHub Discussions](../../discussions) for questions, ideas, and learning support.
- Use [Issues](../../issues) for actionable content problems and feature requests.
- Be constructive, specific, and evidence-based in all feedback.
- Follow the [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

---

## Maintainers

See [CHANGELOG.md](./CHANGELOG.md) for the current maintainers and release history.
