# Syllabus

## GitHub Copilot Pro+ Mastery in VS Code

> Full curriculum reference. For persona-based navigation and shortcut paths, see [LEARNING_PATH.md](./LEARNING_PATH.md).

This curriculum teaches GitHub Copilot Pro+ from first use to full professional mastery. It is structured as a strict linear progression: each level builds on the previous one. Complete the modules in order, do the labs, and check off the completion checklist before advancing.

---

## Curriculum at a Glance

| Level | Modules | Labs | Est. time | Graduates can… |
|-------|---------|------|-----------|----------------|
| 1 — Beginner | 01–03 | 01–03 | ~6 hrs | Use all modes correctly, configure a project, make cost-aware decisions |
| 2 — Intermediate | 04–05 | 04–06 | ~5 hrs | Write structured prompts for any scenario, maintain persistent custom instructions |
| 3 — Advanced | 06–07 | 07–08 | ~6 hrs | Define and operate 10 specialized agents, run coordinated multi-agent workflows |
| 4 — Expert | 08–10 + Capstone | 09–10 | ~7 hrs | Apply all features, govern AI output, build and execute a 90-day adoption roadmap |

---

## Level 1 — Beginner

> **Entry gate:** A GitHub account with an active Copilot subscription. VS Code installed. No prior Copilot experience required.
>
> **Exit outcomes:** Copilot is installed, configured, and working. You can select the right mode for any task, write a project-level instruction file, and evaluate AI-generated code critically before committing it.
>
> **Estimated time:** ~6 hours

### Module 01: Foundations

**Goal:** Install and verify GitHub Copilot Pro+, understand all six interaction modes, and build the habit of critical AI output evaluation.

**Prerequisite:** Active Copilot subscription. VS Code installed.

| Topic | Key skills |
|-------|-----------|
| Installation and authentication | Activate Copilot Pro+ in VS Code, verify status bar |
| Copilot modes overview | Inline completion, Ask, Edit, Plan, Agent, Inline Chat — what each does |
| When to use each mode | Decision criteria based on task type and complexity |
| Evaluating AI output critically | Four-question review gate; never commit unreviewed AI code |
| Key VS Code settings | Essential Copilot settings to configure immediately |

**Lab:** [Lab 01 — Getting Started](./labs/lab-01-getting-started/)
**Deliverable:** Working Copilot setup verified across all major modes

---

### Module 02: Configuration

**Goal:** Configure VS Code and the project for maximum Copilot effectiveness.

**Prerequisite:** Module 01 complete.

| Topic | Key skills |
|-------|-----------|
| VS Code workspace settings | `.vscode/settings.json` for Copilot and editor quality |
| Project-level Copilot instructions | Write `.github/copilot-instructions.md` with specific, verifiable rules |
| Project structure for AI context | File organization, naming, and documentation that strengthen Copilot signals |
| Linting and formatting | Configure tools that give Copilot clean code to learn from |
| Task automation | VS Code tasks for build, test, and lint; agent-accessible via terminal |

**Lab:** [Lab 02 — Project Configuration Baseline](./labs/lab-02-configuration/)
**Deliverable:** `.vscode/` config files, `.github/copilot-instructions.md`, linter, and task runner

---

### Module 03: Token and Premium Request Optimization

**Goal:** Make cost-aware decisions about modes, models, and context from the start.

**Prerequisite:** Modules 01 and 02 complete.

| Topic | Key skills |
|-------|-----------|
| Included vs. premium requests | Which actions consume quota and which do not |
| Model selection framework | When to use GPT-4o, Claude, o1 — and when the default is enough |
| Context window discipline | Keep context minimal, scoped, and unambiguous |
| Compact prompt construction | Goal + constraints + output format in a single turn |
| Mode/model decision framework | Reference table by task type |

**Lab:** [Lab 03 — Token Audit Exercise](./labs/lab-03-token-audit/)
**Deliverable:** Personal mode/model decision cheat sheet

**Level 1 completion:** → [checklists/beginner-completion.md](./checklists/beginner-completion.md)

---

## Level 2 — Intermediate

> **Entry gate:** Level 1 complete. Copilot is running in a configured project. You have a mode/model cheat sheet.
>
> **Exit outcomes:** You write structured, reliable prompts for any coding scenario without follow-ups. You maintain persistent custom instructions at global, project, and path scope. You have a personal prompt library of 10+ tested, reusable prompts.
>
> **Estimated time:** ~5 hours

### Module 04: Prompt Engineering for Coding

**Goal:** Write structured, reliable prompts for every common coding scenario.

**Prerequisite:** Level 1 complete. Module 03 teaches compact prompts — this module builds on that foundation with full scenario coverage.

| Topic | Key skills |
|-------|-----------|
| Prompt architecture | Goal, constraints, output format — the three required components |
| Prompting for code generation | Role, task, format, constraints pattern |
| Prompting for refactoring | Specify what changes; specify what must not change |
| Prompting for debugging | Describe symptoms and context, not just the error message |
| Prompting for tests | Coverage intent, edge cases, framework, assertion style |
| Prompting for documentation | Audience, format, depth, tone |
| Prompting for security review | OWASP scope, threat model, language and framework context |
| Prompt anti-patterns | What causes hallucinations, scope creep, and repetition |

**Lab:** [Lab 04 — Prompt Engineering Workshop](./labs/lab-04-prompt-engineering/)
**Deliverable:** 5 prompt entries committed to `prompts/` using the course prompt template

---

### Module 05: Persistent Custom Instructions

**Goal:** Encode project conventions into stable, reusable Copilot guidance that applies automatically.

**Prerequisite:** Module 04 complete. Writing effective instructions requires the same structural thinking as prompt engineering.

| Topic | Key skills |
|-------|-----------|
| Global instructions | User-level configuration that applies across all projects |
| Repository-wide instructions | `.github/copilot-instructions.md` at project scope |
| Path-specific instructions | `.github/instructions/[name].instructions.md` with `applyTo` frontmatter |
| Instruction design principles | Specific, bounded, imperative, non-contradictory |
| Testing instructions | Verify Copilot reads and applies them; fix when they are ignored |
| Maintenance | Version, audit, and update instructions as the codebase evolves |

**Lab:** [Lab 05 — Write Your Project's Custom Instructions](./labs/lab-05-custom-instructions/)
**Deliverable:** Complete `instructions/` folder for a sample project with 3 scoped examples

**Level 2 completion:** → [checklists/intermediate-completion.md](./checklists/intermediate-completion.md)

---

## Level 3 — Advanced

> **Entry gate:** Level 2 complete. Structured prompting is a consistent habit. Custom instructions are in place on at least one real project.
>
> **Exit outcomes:** You can define a role-specialized agent persona with tool permissions and handoff protocol. You can decompose a complex multi-step task into a bounded agent workflow, execute it, and know when to stop. You have all 10 agent definitions in your `agents/` folder.
>
> **Estimated time:** ~6 hours

### Module 06: Agents and Role Specialization

**Goal:** Define and operate 10 specialized agent personas with clear responsibilities, tool permissions, and handoff protocols.

**Prerequisite:** Level 2 complete. Agents are persistent custom instructions combined with tool access — both concepts must be solid before agent work.

**10 agent personas:**

| Agent | Core responsibility |
|-------|-------------------|
| Planner / Analyst | Decompose work, identify risks, define tasks |
| Solution Architect | Design system structure, define component boundaries |
| Implementer / Developer | Write and integrate code to spec |
| Refactoring Specialist | Improve internal structure without changing behavior |
| Code Reviewer | Enforce standards, catch issues before merge |
| Security Reviewer | Identify vulnerabilities, apply OWASP patterns |
| Test Engineer | Design and write tests for correctness and coverage |
| Documentation Writer | Produce clear, accurate, audience-aware documentation |
| Performance Optimizer | Profile and improve speed and resource usage |
| DevOps / Release Assistant | CI/CD, deployment, and infrastructure tasks |

**Topics covered:**

| Topic | Key skills |
|-------|-----------|
| Agent anatomy | Role, scope, tool permissions, exit conditions, handoff protocol |
| Tool permission model | Allow / conditional / deny — and why each boundary exists |
| Running a single-agent session | Set scope, execute, evaluate output, know when to stop |
| Agent session prompts | How to open and close an agent session cleanly |

**Lab:** [Lab 07 — Define and Run Your First Agent Session](./labs/lab-07-first-agent-session/)
**Deliverable:** All 10 agent definitions in `/agents/`

---

### Module 07: Multi-Agent Workflows

**Goal:** Orchestrate multiple agents on complex tasks without context pollution, duplicate work, or runaway sessions.

**Prerequisite:** Module 06 complete. All 10 agent definitions must exist before workflows can be designed.

| Topic | Key skills |
|-------|-----------|
| Task decomposition | Break problems into bounded, handoff-ready chunks |
| Workflow 1 — Feature delivery | Planner → Architect → Implementer → Code Reviewer |
| Workflow 2 — Bug investigation | Analyst → Implementer → Test Engineer → Code Reviewer |
| Workflow 3 — Refactor and validate | Refactoring Specialist → Test Engineer → Code Reviewer |
| Handoff protocols | What to pass between agents, how to summarize, when to stop |
| Context hygiene | Prevent context pollution and duplicate work across sessions |

**Lab:** [Lab 08 — Run a Complete Multi-Agent Workflow](./labs/lab-08-multi-agent-workflow/)
**Deliverable:** One documented, repeatable workflow file in `/agents/`

**Level 3 completion:** → [checklists/advanced-completion.md](./checklists/advanced-completion.md)

---

## Level 4 — Expert

> **Entry gate:** Level 3 complete. You have run at least one multi-agent workflow end-to-end.
>
> **Exit outcomes:** You apply all Copilot features with deliberate intent. You can audit a repository for AI-friendliness and fix what you find. You have a written, actionable 90-day personal or team adoption plan. The capstone is complete.
>
> **Estimated time:** ~7 hours

### Module 08: Advanced Features

**Goal:** Leverage Plan mode, AI-assisted review, terminal integration, and CI/CD connections professionally.

**Prerequisite:** Level 3 complete.

| Topic | Key skills |
|-------|-----------|
| Plan mode | Use Copilot to design a solution before writing a single line |
| AI-assisted code review | Systematic review workflow with Copilot in the loop |
| Terminal and CLI integration | Copilot in the terminal; command explanations and suggestions |
| Test runner integration | Copilot with pytest, Jest, xUnit, and equivalent frameworks |
| CI/CD integration | Copilot in pipelines, PR guidance, automated code scanning |
| Large codebase strategies | Scope context effectively in repositories with hundreds of files |
| Secure usage patterns | Secrets hygiene, sensitive code handling, confidentiality boundaries |

**Lab:** [Lab 09 — Advanced Feature Tour](./labs/lab-09-advanced-feature-tour/)
**Deliverable:** CI/CD integration notes and a completed secure-usage checklist

---

### Module 09: Repository Quality for AI

**Goal:** Keep repositories AI-friendly, clearly structured, and governed for the long term.

**Prerequisite:** Module 08 complete.

| Topic | Key skills |
|-------|-----------|
| AI-friendly repository design | Eliminate noise, ambiguity, and mixed-concern files |
| Documentation quality | READMEs and inline docs that serve both humans and AI context |
| Governance of AI-generated code | Review protocols, ownership, and traceability standards |
| Naming and structure conventions | Patterns that maximize AI context signal across the codebase |
| Pre-merge validation | The minimum human check before every AI-assisted commit |

**Lab:** [Lab 10 — Repository Health Audit](./labs/lab-10-repository-health-audit/)
**Deliverable:** Completed AI output review checklist applied to a real project

---

### Module 10: Adoption Roadmap

**Goal:** Plan and execute a personal or team Copilot adoption across 7, 30, 60, and 90 days.

**Prerequisite:** Modules 08 and 09 complete. This is a synthesis module — it is only meaningful with the full skill set.

| Timeframe | Focus | Gate deliverable |
|-----------|-------|-----------------|
| 7 days | Setup, verification, first real usage | Level 1 complete; cheat sheet in use |
| 30 days | Prompt discipline, custom instructions live | Personal prompt library + `instructions/` folder |
| 60 days | Agent workflows, advanced features in production | 10 agent definitions + first multi-agent run |
| 90 days | Full mastery, governance, team rollout ready | Capstone complete; adoption plan written and shared |

**Capstone:** [/capstone](./capstone/)

**Level 4 completion:** → [checklists/expert-completion.md](./checklists/expert-completion.md)

---

## Module Dependency Map

```
01-foundations
      │
02-configuration
      │
03-token-optimization
      │
04-prompt-engineering
      │
05-custom-instructions
      │
06-agents
      │
07-multi-agent-workflows
      │
08-advanced-features
      │
09-repository-quality
      │
10-adoption-roadmap
      │
  Capstone
```

Dependencies are **strict and linear.** No module can be skipped. Each module's exercises require the skills from all previous modules.

For persona-based navigation and shortcut paths, see [LEARNING_PATH.md](./LEARNING_PATH.md).

→ For a persona-based navigation, see [LEARNING_PATH.md](./LEARNING_PATH.md).
