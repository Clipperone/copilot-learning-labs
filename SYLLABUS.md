# Syllabus

## GitHub Copilot Pro+ Mastery in VS Code

> Full curriculum reference. For navigation by learning path, see [LEARNING_PATH.md](./LEARNING_PATH.md).

---

## Level 1 — Beginner

### Module 01: Foundations
**Goal:** Understand what GitHub Copilot is, install and verify it, and learn to evaluate AI output critically.

| Topic | Key skills |
|-------|-----------|
| Installation and authentication | Activate Copilot Pro+ in VS Code, verify status |
| Copilot modes overview | Inline completion, chat, ask, edit, plan, agent — what each does |
| When to use each mode | Decision criteria based on task type and complexity |
| Evaluating AI output | Critical review checklist, trust but verify mindset |
| Key VS Code settings | Essential Copilot settings to configure immediately |

**Lab:** [Lab 01 — Setup and Verify](./labs/lab-01-setup-and-verify/)
**Deliverable:** Working Copilot setup + personal evaluation checklist

---

### Module 02: Configuration
**Goal:** Configure VS Code and your project for maximum Copilot effectiveness.

| Topic | Key skills |
|-------|-----------|
| Ideal VS Code setup | Settings, keybindings, layout for AI-assisted work |
| Recommended extensions | Complementary tools that improve Copilot context |
| Project structure for AI | File organization, naming, documentation baseline |
| Linting and formatting | Configure tools that give Copilot clean code signals |
| Task automation | VS Code tasks and terminal integration |

**Lab:** Lab 02 — Project Configuration Baseline
**Deliverable:** `.vscode/` config files, documented project structure

---

### Module 03: Token and Premium Request Optimization
**Goal:** Make cost-aware decisions about modes, models, and context.

| Topic | Key skills |
|-------|-----------|
| What consumes tokens | Inline vs. chat vs. agent cost comparison |
| Included vs. premium models | When to use GPT-4o, Claude, o1, and when not to |
| Efficient context strategies | Keep context minimal, focused, and unambiguous |
| Compact prompts | Write short prompts that produce complete results |
| Decision framework | Mode/model selector by task type |

**Lab:** Lab 03 — Token Audit Exercise
**Deliverable:** Personal mode/model decision cheat sheet

---

## Level 2 — Intermediate

### Module 04: Prompt Engineering for Coding
**Goal:** Write structured, reliable prompts for every common coding scenario.

| Topic | Key skills |
|-------|-----------|
| Prompting for code generation | Role, task, format, constraints pattern |
| Prompting for refactoring | Specify what changes, what must not change |
| Prompting for debugging | Describe symptoms, not just errors |
| Prompting for tests | Coverage intent, edge cases, framework |
| Prompting for docs and review | Audience, format, depth |
| Prompting for security review | OWASP scope, threat model, language/framework |
| Prompt anti-patterns | What causes hallucinations, scope creep, repetition |

**Lab:** Lab 04 — Prompt Patterns Workshop
**Lab:** Lab 05 — Build a Personal Prompt Library
**Deliverable:** 10+ personal prompts in `/prompts/`

---

### Module 05: Persistent Custom Instructions
**Goal:** Encode project conventions into stable, reusable guidance for Copilot.

| Topic | Key skills |
|-------|-----------|
| Global instructions | User-level `.github/copilot-instructions.md` |
| Repository-wide instructions | Project-level Copilot behavior |
| Path-specific instructions | Different rules for different parts of the codebase |
| Agent-specific instructions | Override instructions per agent session |
| Instruction design principles | Be specific, be bounded, avoid contradictions |

**Lab:** Lab 06 — Write Your Project's Custom Instructions
**Deliverable:** Complete `instructions/` folder for a sample project

---

## Level 3 — Advanced

### Module 06: Agents and Role Specialization
**Goal:** Define and operate 10 specialized agent personas with clear responsibilities and handoffs.

Personas covered:

| Agent | Purpose |
|-------|---------|
| Planner / Analyst | Break down work, identify risks, define tasks |
| Solution Architect | Design system structure, define boundaries |
| Implementer / Developer | Write and integrate code |
| Refactoring Specialist | Improve internal structure without changing behavior |
| Code Reviewer | Enforce standards, catch issues before merge |
| Security Reviewer | Identify vulnerabilities, apply OWASP patterns |
| Test Engineer | Design and write tests for correctness and coverage |
| Documentation Writer | Produce clear, accurate, audience-aware docs |
| Performance Optimizer | Profile and improve speed and resource usage |
| Release / DevOps Assistant | CI/CD, deployment, infrastructure tasks |

**Lab:** Lab 07 — Define and Run Your First Agent Session
**Deliverable:** All 10 agent definitions in `/agents/`

---

### Module 07: Multi-Agent Workflows
**Goal:** Orchestrate multiple agents on complex tasks without duplication or context pollution.

| Topic | Key skills |
|-------|-----------|
| Decomposing complex tasks | Break problems into bounded, handoff-ready chunks |
| Workflow 1: New feature delivery | Planner → Architect → Implementer → Reviewer |
| Workflow 2: Complex bug fixing | Analyst → Implementer → Test Engineer → Reviewer |
| Workflow 3: Refactoring + testing + review | Refactoring Specialist → Test Engineer → Code Reviewer |
| Context hygiene | Avoid polluted context, duplicate work, and wasted requests |
| Handoff protocols | What to pass, how to summarize, when to stop |

**Lab:** Lab 08 — Run a Complete Multi-Agent Workflow
**Deliverable:** Documented, repeatable workflow file in `/agents/`

---

## Level 4 — Expert

### Module 08: Advanced Features
**Goal:** Leverage planning mode, AI review, terminal integration, and CI/CD connections.

| Topic | Key skills |
|-------|-----------|
| Plan mode | Use Copilot to design before implementing |
| AI-assisted code review | Systematic review with Copilot in the loop |
| Terminal and CLI integration | Copilot in the terminal, command suggestions |
| Test runner integration | Copilot with Jest, pytest, xUnit, etc. |
| CI/CD integration | Copilot in pipelines, code scanning, PR guidance |
| Context on large repositories | Strategies for big codebases with many files |
| Secure usage patterns | Handling sensitive code, secrets hygiene, confidentiality |

**Lab:** Lab 09 — Advanced Feature Tour
**Deliverable:** CI/CD integration notes, security usage checklist

---

### Module 09: Repository Quality for AI
**Goal:** Keep repositories AI-friendly, architecturally sound, and maintainable long-term.

| Topic | Key skills |
|-------|-----------|
| AI-friendly repositories | Reduce noise and ambiguity Copilot picks up |
| README and docs quality | Write docs that help both humans and AI |
| Governance of AI-generated code | Personal review protocols before commit |
| Human validation checklist | What to always verify before merge |
| Naming and structure conventions | Patterns that improve AI context signal |

**Lab:** Lab 10 — Repository Health Audit
**Deliverable:** Completed `checklists/ai-output-review.md` for your project

---

### Module 10: Adoption Roadmap
**Goal:** Build and execute a personal or team adoption plan across 7, 30, 60, and 90 days.

| Timeframe | Focus | Key deliverable |
|-----------|-------|----------------|
| 7 days | Setup, baseline, first real usage | Verified config + Module 01–02 complete |
| 30 days | Prompt discipline, custom instructions | Prompt library + instructions/ folder |
| 60 days | Agent workflows, advanced features | Agent definitions + first multi-agent run |
| 90 days | Full mastery, governance, team rollout | Capstone complete + adoption plan published |

**Capstone:** [/capstone](./capstone/)

---

## Navigation Map

```
Module 01 → Module 02 → Module 03
                ↓
           Module 04 → Module 05
                ↓
           Module 06 → Module 07
                ↓
      Module 08 → Module 09 → Module 10
                                  ↓
                              Capstone
```

→ For a persona-based navigation, see [LEARNING_PATH.md](./LEARNING_PATH.md).
