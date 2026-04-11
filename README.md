# copilot-learning-labs

> **From first autocomplete to production-grade AI-assisted workflows.**

An open, self-paced course on **GitHub Copilot Pro+** in **Visual Studio Code**.
Clone this repository, follow the labs, and apply the templates directly to your own projects — no registration, no LMS, no cost beyond your Copilot subscription.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Release](https://img.shields.io/badge/release-v0.1--foundation-green)](./CHANGELOG.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](./CONTRIBUTING.md)

---

## Getting Started

**Requirements:** GitHub account with **GitHub Copilot Pro+** active · VS Code 1.90+

```bash
git clone https://github.com/Clipperone/copilot-learning-labs.git
cd copilot-learning-labs
```

Open the folder in VS Code, install the recommended extensions when prompted, and sign in to GitHub.

**Then start here → [LEARNING_PATH.md](./LEARNING_PATH.md)**

Or jump straight to the first lab → [labs/lab-01-getting-started/](./labs/lab-01-getting-started/) · [Browse all labs](./labs/)

> Most beginner and intermediate content works on any paid Copilot plan. Agent mode and premium model access require **Pro+**. Plan-specific restrictions are noted at the module level.

---

## Who This Course Is For

| Learner | Starting point | Primary goal |
|---------|---------------|-------------|
| Developer new to Copilot | No Copilot experience | Get productive fast with a structured foundation |
| Developer using Copilot informally | Uses completions and basic chat | Move from ad hoc usage to deliberate, repeatable workflows |
| Engineering manager | Team has Copilot, no standards | Define team conventions, instructions, and adoption milestones |
| Developer productivity coach | Copilot experience, no training framework | Build and deliver a structured, practical training program |

**Prerequisite knowledge:** Basic familiarity with VS Code and at least one programming language. No prior Copilot experience required.

**Plan requirement:** Most beginner and intermediate content applies to all paid Copilot plans. Agent mode, premium model access, and some advanced features require **GitHub Copilot Pro+**. Plan-specific restrictions are noted at the module level.

---

## What You Will Learn

- Configure GitHub Copilot Pro+ and VS Code for maximum productivity
- Choose the right Copilot mode — inline completion, chat, ask, edit, plan, agent — for any task
- Write effective, repeatable prompts for code generation, refactoring, debugging, testing, documentation, and security review
- Design persistent custom instructions that guide Copilot consistently across a project
- Define role-specialized agents with clear responsibilities, tool permissions, and handoff protocols
- Orchestrate multi-agent workflows on complex, multi-step tasks without wasting context or requests
- Make cost-aware decisions about models and modes to minimize premium request consumption
- Apply a structured 7/30/60/90-day personal adoption roadmap

---

## Quick Navigation

| I want to… | Go to |
|-----------|-------|
| Follow the course from the beginning | [LEARNING_PATH.md](./LEARNING_PATH.md) |
| See all modules and topics at a glance | [SYLLABUS.md](./SYLLABUS.md) |
| Start the first lab immediately | [labs/lab-01-getting-started/](./labs/lab-01-getting-started/) |
| Find a reusable prompt | [prompts/](./prompts/) |
| Read the full course overview | [COURSE_OVERVIEW.md](./COURSE_OVERVIEW.md) |
| Review AI-generated code safely | [checklists/ai-output-review.md](./checklists/ai-output-review.md) |
| Understand what was recently added | [CHANGELOG.md](./CHANGELOG.md) |

---

## Course Structure

The course is organized into **10 progressive modules** across 4 levels, each paired with a hands-on lab and a self-assessment checklist.

| Level | Modules | Focus |
|-------|---------|-------|
| **Beginner** | 01 — 03 | Setup, configuration, token and cost awareness |
| **Intermediate** | 04 — 05 | Prompt engineering, custom instructions |
| **Advanced** | 06 — 07 | Agent personas, multi-agent workflows |
| **Expert** | 08 — 10 | Advanced features, repository quality, adoption planning |

### Modules

| # | Module | Level | Key skill |
|---|--------|-------|-----------|
| 01 | [Foundations](./modules/01-foundations/) | Beginner | Install, verify, understand all modes, evaluate AI output |
| 02 | [Configuration](./modules/02-configuration/) | Beginner | Optimize VS Code and project structure for AI context |
| 03 | [Token Optimization](./modules/03-token-optimization/) | Beginner | Mode/model decision framework, cost-aware workflows |
| 04 | [Prompt Engineering](./modules/04-prompt-engineering/) | Intermediate | Structured prompts for every coding scenario |
| 05 | [Custom Instructions](./modules/05-custom-instructions/) | Intermediate | Persistent guidance at global, project, and path scope |
| 06 | [Agents and Role Specialization](./modules/06-agents/) | Advanced | 10 role-specialized personas with tool permissions and handoffs |
| 07 | [Multi-Agent Workflows](./modules/07-multi-agent-workflows/) | Advanced | Orchestrate agents across complex, multi-step tasks |
| 08 | Advanced Features | Expert | Plan mode, AI review, terminal integration, CI/CD |
| 09 | Repository Quality | Expert | AI-friendly project structure, governance, review protocols |
| 10 | Adoption Roadmap | Expert | 7/30/60/90-day personal and team adoption plan |

Modules 04–10 are being released progressively. See the [roadmap](#roadmap) below.

### Labs

| Lab | Paired module | Status |
|-----|--------------|--------|
| [Lab 01 — Getting Started](./labs/lab-01-getting-started/) | Module 01 | ✅ Available |
| [Lab 02 — Project Configuration Baseline](./labs/lab-02-configuration/) | Module 02 | ✅ Available |
| [Lab 03 — Token Audit](./labs/lab-03-token-audit/) | Module 03 | ✅ Available |
| [Lab 04 — Prompt Engineering Workshop](./labs/lab-04-prompt-engineering/) | Module 04 | ✅ Available |
| [Lab 05 — Write Your Project's Custom Instructions](./labs/lab-05-custom-instructions/) | Module 05 | ✅ Available |
| [Lab 06 — Agents and Personas](./labs/lab-06-agents-and-personas/) | Module 06 | ✅ Available |
| [Lab 07 — Run a Complete Multi-Agent Workflow](./labs/lab-07-multi-agent-workflow/) | Module 07 | ✅ Available |
| [Lab 08 — Advanced Feature Tour](./labs/lab-08-advanced-feature-tour/) | Module 08 | ✅ Available |
| Lab 09 — Repository Health Audit | Module 09 | Planned — v1.0 |

---

## Repository Contents

| Folder / File | Purpose |
|---------------|---------|
| [modules/](./modules/) | Learning modules — theory, exercises, and checklists |
| [labs/](./labs/) | Hands-on labs — starter files and reference solutions |
| [prompts/](./prompts/) | Reusable prompt library by category |
| [instructions/](./instructions/) | Custom instruction examples *(coming in v0.3)* |
| [agents/](./agents/) | Agent persona definitions — populated during Lab 06 |
| [templates/](./templates/) | Authoring templates for all content types |
| [checklists/](./checklists/) | AI output review, pre-commit, and completion checklists |
| [docs/](./docs/) | Architecture decisions and design reference |
| [capstone/](./capstone/) | Final project *(coming in v1.0)* |
| [COURSE_OVERVIEW.md](./COURSE_OVERVIEW.md) | Scope, audience, and key outcomes |
| [SYLLABUS.md](./SYLLABUS.md) | Full 10-module curriculum detail |
| [LEARNING_PATH.md](./LEARNING_PATH.md) | Guided navigation by level and persona |
| [CONTRIBUTING.md](./CONTRIBUTING.md) | How to contribute |
| [CHANGELOG.md](./CHANGELOG.md) | Release history |

---

## Roadmap

| Release | Status | Contents |
|---------|--------|---------|
| `v0.1` — Foundation | ✅ Released | Module 01, Lab 01, all templates, prompt starter set, checklists, `.github/` and `.vscode/` config |
| `v0.2` — Beginner complete | ✅ Released | Modules 02–03, Labs 02–03, additional prompts |
| `v0.3` — Intermediate complete | ✅ Released | Modules 04–05, Labs 04–05, `instructions/` folder |
| `v0.4` — Advanced complete | **Current** | Module 06–07, Lab 06, `agents/` folder |
| `v1.0` — Full course | Planned | All 10 modules, Labs 09–10, capstone, examples, FAQ |

Feature requests and content suggestions are tracked as [GitHub Issues](../../issues). Use the [content suggestion template](./.github/ISSUE_TEMPLATE/content_suggestion.md) to propose new material.

---

## Contributing

Contributions of all kinds are welcome — content fixes, new prompts, improved labs, and translation notes.

Before opening a PR:

1. Read [CONTRIBUTING.md](./CONTRIBUTING.md) for conventions and template requirements.
2. For significant changes, open an issue first.
3. Follow the [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

Use [GitHub Discussions](../../discussions) for questions, learning support, and ideas that are not yet ready for an issue.

---

## Feature Verification

This course documents GitHub Copilot features as they exist at publication time. Each module includes a `Verified: YYYY-MM` date. Copilot evolves quickly — if you find outdated content, open a [bug report](./.github/ISSUE_TEMPLATE/bug_report.md).

Official references:

- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot documentation](https://code.visualstudio.com/docs/copilot/overview)
- [GitHub Copilot changelog](https://github.blog/changelog/label/copilot/)

---

## License

[MIT](./LICENSE) — free to use, adapt, and share with attribution.
