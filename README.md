# GitHub Copilot Learning Labs

> **From first autocomplete to production-grade AI-assisted workflows.**

An open, self-paced course on **GitHub Copilot Pro+** in **Visual Studio Code**.
Clone this repository, follow the labs, and apply the templates directly to your own projects — no registration, no LMS, no cost beyond your Copilot subscription.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Release](https://img.shields.io/badge/release-v1.0--full--course-green)](./CHANGELOG.md)
[![VS Code](https://img.shields.io/badge/VS%20Code-1.90%2B-007ACC)](https://code.visualstudio.com/)
[![Copilot](https://img.shields.io/badge/GitHub%20Copilot-Pro%2B-8957e5)](https://github.com/features/copilot)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](./CONTRIBUTING.md)
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-ea4aaa)](https://github.com/sponsors/Clipperone)

---

## Contents

- [Getting Started](#getting-started)
- [Who This Course Is For](#who-this-course-is-for)
- [What You Will Learn](#what-you-will-learn)
- [Quick Navigation](#quick-navigation)
- [Course Structure](#course-structure)
- [Repository Contents](#repository-contents)
- [Contributing](#contributing)
- [Feature Verification](#feature-verification)
- [License](#license)

---

## Getting Started

**Requirements:** GitHub account with **GitHub Copilot Pro+** active · VS Code 1.90+

```bash
git clone https://github.com/Clipperone/copilot-learning-labs.git
cd copilot-learning-labs
```

Open the folder in VS Code, install the recommended extensions when prompted, and sign in to GitHub.

**Then start here → [LEARNING_PATH.md](./LEARNING_PATH.md)**

> [!NOTE]
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

---

## What You Will Learn

| Skill area | What you will be able to do |
|------------|----------------------------|
| **Setup and modes** | Configure Copilot Pro+ and VS Code for maximum productivity; choose the right mode — inline completion, inline chat, Ask, Plan, Agent — for any task |
| **Prompt engineering** | Write effective, repeatable prompts for code generation, refactoring, debugging, testing, documentation, and security review |
| **Custom instructions** | Design persistent instructions that guide Copilot consistently across a project at global, project, and path scope |
| **Agent workflows** | Define role-specialized agents with clear responsibilities, tool permissions, and handoff protocols |
| **Multi-agent orchestration** | Orchestrate agents across complex, multi-step tasks without wasting context or premium requests |
| **Cost awareness** | Make cost-aware decisions about models and modes to minimize premium request consumption |
| **Adoption planning** | Apply a structured 7/30/60/90-day personal and team adoption roadmap |

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

**10 progressive modules** across 4 levels, each paired with a hands-on lab and a self-assessment checklist.

| # | Module | Level | Lab | Key skill |
|---|--------|-------|-----|-----------|
| 01 | [Foundations](./modules/01-foundations/) | Beginner | [Lab 01 — Getting Started](./labs/lab-01-getting-started/) | Install, verify, understand all modes, evaluate AI output |
| 02 | [Configuration](./modules/02-configuration/) | Beginner | [Lab 02 — Project Configuration Baseline](./labs/lab-02-configuration/) | Optimize VS Code and project structure for AI context |
| 03 | [Token Optimization](./modules/03-token-optimization/) | Beginner | [Lab 03 — Token Audit](./labs/lab-03-token-audit/) | Mode/model decision framework, cost-aware workflows |
| 04 | [Prompt Engineering](./modules/04-prompt-engineering/) | Intermediate | [Lab 04 — Prompt Engineering Workshop](./labs/lab-04-prompt-engineering/) | Structured prompts for every coding scenario |
| 05 | [Custom Instructions](./modules/05-custom-instructions/) | Intermediate | [Lab 05 — Write Your Project's Custom Instructions](./labs/lab-05-custom-instructions/) | Persistent guidance at global, project, and path scope |
| 06 | [Agents and Role Specialization](./modules/06-agents/) | Advanced | [Lab 06 — Agents and Personas](./labs/lab-06-agents-and-personas/) | 10 role-specialized personas with tool permissions and handoffs |
| 07 | [Multi-Agent Workflows](./modules/07-multi-agent-workflows/) | Advanced | [Lab 07 — Run a Complete Multi-Agent Workflow](./labs/lab-07-multi-agent-workflow/) | Orchestrate agents across complex, multi-step tasks |
| 08 | [Advanced Features](./modules/08-advanced-features/) | Expert | [Lab 08 — Advanced Feature Tour](./labs/lab-08-advanced-feature-tour/) | Plan mode, AI review, terminal integration, CI/CD |
| 09 | [AI-Friendly Repository Engineering](./modules/09-repository-quality/) | Expert | [Lab 09 — Repository Health Audit](./labs/lab-09-repository-health-audit/) | AI-friendly project structure, governance, review protocols |
| 10 | [Adoption Roadmap](./modules/10-adoption-roadmap/) | Expert | [Capstone](./capstone/) | 7/30/60/90-day personal and team adoption plan |
| 11 | [Platform & GitHub.com Integration](./modules/11-platform-integration/) | Expert | [Capstone](./capstone/) (Deliverable 8) | Coding agent, Copilot in github.com, `gh copilot` CLI, surface decisions |

---

## Repository Contents

| Folder / File | Purpose |
|---------------|---------|
| [modules/](./modules/) | Learning modules — theory, exercises, and checklists |
| [labs/](./labs/) | Hands-on labs — starter files and reference solutions |
| [prompts/](./prompts/) | Reusable prompt library by category |
| [instructions/](./instructions/) | Custom instruction examples (global, project, path-scoped) |
| [agents/](./agents/) | Agent persona definitions — populated during Lab 06 |
| [templates/](./templates/) | Authoring templates for all content types |
| [checklists/](./checklists/) | AI output review, pre-commit, and completion checklists |
| [docs/](./docs/) | Architecture decisions and design reference |
| [capstone/](./capstone/) | Final project — End-to-End Copilot Workflow Integration |
| [COURSE_OVERVIEW.md](./COURSE_OVERVIEW.md) | Scope, audience, and key outcomes |
| [SYLLABUS.md](./SYLLABUS.md) | Full 10-module curriculum detail |
| [LEARNING_PATH.md](./LEARNING_PATH.md) | Guided navigation by level and persona |
| [CONTRIBUTING.md](./CONTRIBUTING.md) | How to contribute |
| [CHANGELOG.md](./CHANGELOG.md) | Release history |

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
