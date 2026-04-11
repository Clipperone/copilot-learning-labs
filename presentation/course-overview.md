---
marp: true
theme: default
paginate: true
---

# GitHub Copilot Learning Labs

### From first autocomplete to production-grade AI-assisted workflows.

An open, self-paced course on **GitHub Copilot Pro+** in **Visual Studio Code**

github.com/Clipperone/copilot-learning-labs

---

## Who This Course Is For

| Persona | Starting point | Primary goal |
|---------|---------------|-------------|
| Individual developer | Little or no Copilot experience | Personal productivity and code quality |
| Engineering manager | Wants team standardization | Define team conventions and adoption plan |
| Developer productivity coach | Copilot experience, no structure | Build a repeatable training framework |
| Senior developer | Experienced user, no system | Move from ad hoc usage to deliberate AI workflows |

**Prerequisite:** Familiarity with VS Code and at least one programming language. No prior Copilot experience required.

---

## What You Will Learn

| Skill area | What you will be able to do |
|------------|----------------------------|
| **Setup and modes** | Configure Copilot Pro+ and VS Code; choose the right mode for any task |
| **Prompt engineering** | Write reliable prompts for generation, refactoring, debugging, testing, docs, and security review |
| **Custom instructions** | Encode project conventions into persistent guidance at global, project, and path scope |
| **Agent workflows** | Define role-specialized agents with tool permissions and handoff protocols |
| **Multi-agent orchestration** | Orchestrate agents on complex tasks without context pollution or wasted requests |
| **Cost awareness** | Make cost-aware decisions about models and modes |
| **Adoption planning** | Build and execute a 7/30/60/90-day personal or team adoption roadmap |

---

## Course Map — 10 Modules, 4 Levels

| Level | Modules | Est. time | Graduates can… |
|-------|---------|-----------|----------------|
| **Beginner** | 01–03 | ~6 hrs | Use all modes, configure a project, make cost-aware decisions |
| **Intermediate** | 04–05 | ~5 hrs | Write structured prompts for any scenario; maintain custom instructions |
| **Advanced** | 06–07 | ~6 hrs | Define 10 agents; run coordinated multi-agent workflows |
| **Expert** | 08–10 + Capstone | ~7 hrs | Apply all features, govern AI output, produce 7 committed deliverables |

Dependencies are **strict and linear.** Each level builds on the previous one.

---

## Level 1 — Beginner

| # | Module | Key skill |
|---|--------|-----------|
| 01 | Foundations | Install, verify, understand all modes, evaluate AI output |
| 02 | Configuration | Optimize VS Code and project structure for AI context |
| 03 | Token Optimization | Mode/model decision framework, cost-aware workflows |

**Exit deliverables:**
- Working Copilot Pro+ setup verified across all modes
- `.github/copilot-instructions.md` with 3+ specific rules
- Personal mode/model decision cheat sheet

---

## Level 2 — Intermediate

| # | Module | Key skill |
|---|--------|-----------|
| 04 | Prompt Engineering | Structured prompts for every coding scenario |
| 05 | Custom Instructions | Persistent guidance at global, project, and path scope |

**Exit deliverables:**
- 5 prompt entries committed to `prompts/` using the course template
- `instructions/` folder with global, project, and path-scoped examples

---

## Level 3 — Advanced

| # | Module | Key skill |
|---|--------|-----------|
| 06 | Agents and Role Specialization | 10 role-specialized personas with tool permissions and handoffs |
| 07 | Multi-Agent Workflows | Orchestrate agents across complex, multi-step tasks |

**Exit deliverables:**
- All 10 agent definitions committed to `agents/`
- One documented, repeatable multi-agent workflow file

---

## Level 4 — Expert

| # | Module | Key skill |
|---|--------|-----------|
| 08 | Advanced Features | Plan mode, AI review, terminal integration, CI/CD |
| 09 | AI-Friendly Repository Engineering | AI-friendly project structure, governance, review protocols |
| 10 | Adoption Roadmap | 7/30/60/90-day personal and team adoption plan |

**Exit deliverables:**
- Capstone project complete and self-assessed
- Written 90-day adoption roadmap
- `checklists/expert-completion.md` fully checked

---

## Lab Structure

Every module is paired with a hands-on lab. Each lab contains exactly:

| Item | Purpose |
|------|---------|
| `README.md` | Objective, prerequisites, numbered tasks, success criteria |
| `checklist.md` | Completion self-assessment |
| `starter/` | Files the learner begins with |
| `solution/` | Reference answer — check only after completing the lab |

**9 labs available** — Lab 01 through Lab 09, each paired with its module.

---

## Reusable Assets

Everything you produce is usable in your own projects immediately.

| Folder | Contents |
|--------|---------|
| `prompts/` | Reusable prompt library by category |
| `agents/` | Agent persona definitions — populated during Lab 06 |
| `instructions/` | Custom instruction examples at global, project, and path scope |
| `templates/` | Authoring templates for all content types |
| `checklists/` | AI output review, pre-commit, and completion checklists |

---

## Capstone — 7 Deliverables

Apply every skill from the course to a single project context.

| # | Deliverable | Module |
|---|-------------|--------|
| 1 | `.github/copilot-instructions.md` — ≥5 declarative rules | M05 |
| 2 | `CONVENTIONS.md` — governance policy, ≥5 rules | M09 |
| 3 | `agents/` — ≥3 agent definitions with permissions and handoffs | M06 |
| 4 | `prompts/` — ≥3 prompt entries with filled examples | M04 |
| 5 | `agents/workflow-[name].md` — one multi-agent workflow | M07 |
| 6 | `capstone/validation-report.md` — 5-gate pre-merge validation | M08/M09 |
| 7 | `capstone/roadmap.md` — 90-day adoption plan | M10 |

---

## Getting Started

**Requirements:** GitHub account with GitHub Copilot Pro+ active · VS Code 1.90+

```bash
git clone https://github.com/Clipperone/copilot-learning-labs.git
cd copilot-learning-labs
```

1. Open the folder in VS Code
2. Install the recommended extensions when prompted and sign in to GitHub
3. Open **[LEARNING_PATH.md](../LEARNING_PATH.md)** and self-place to find your starting module

> Most beginner and intermediate content works on any paid Copilot plan.
> Agent mode and premium model access require **Pro+**.

---

## Start Learning

**github.com/Clipperone/copilot-learning-labs**

- License: MIT — free to use, adapt, and share with attribution
- Contributions welcome — see `CONTRIBUTING.md`
- Support the project: **github.com/sponsors/Clipperone**
