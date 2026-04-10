# Learning Path

## GitHub Copilot Pro+ Mastery in VS Code

Choose the path that matches your starting point and goal.

---

## Path 1 — Complete Beginner

**You:** New to GitHub Copilot. Want to use it productively from day one.
**Goal:** Get set up, understand the modes, learn the basics of prompting.
**Time commitment:** ~6 hours across the beginner modules + labs.

```
Module 01: Foundations
    └── Lab 01: Setup and Verify
Module 02: Configuration
    └── Lab 02: Project Configuration Baseline
Module 03: Token Optimization
    └── Lab 03: Token Audit Exercise
    └── checklists/beginner-completion.md ← self-assess here
```

**Next step after this path:** → Path 2 (Intermediate)

---

## Path 2 — Intermediate Developer

**You:** Copilot is working. You use inline completion and basic chat. You want to be more deliberate.
**Goal:** Write structured prompts, create custom instructions, build a personal prompt library.
**Prerequisite:** Completed Path 1 or equivalent experience.
**Time commitment:** ~5 hours.

```
Module 04: Prompt Engineering
    └── Lab 04: Prompt Patterns Workshop
    └── Lab 05: Build a Personal Prompt Library
Module 05: Custom Instructions
    └── Lab 06: Write Your Project's Custom Instructions
```

**Next step after this path:** → Path 3 (Advanced)

---

## Path 3 — Advanced Practitioner

**You:** Comfortable with prompting and custom instructions. Want to use agents and multi-step workflows.
**Goal:** Define role-specialized agents, run agent sessions, orchestrate multi-agent workflows.
**Prerequisite:** Completed Path 2 or equivalent experience.
**Time commitment:** ~6 hours.

```
Module 06: Agents and Role Specialization
    └── Lab 07: Define and Run Your First Agent Session
Module 07: Multi-Agent Workflows
    └── Lab 08: Run a Complete Multi-Agent Workflow
```

**Next step after this path:** → Path 4 (Expert)

---

## Path 4 — Expert / Full Mastery

**You:** Advanced practitioner. Want to leverage all features, harden your practices, and build a team adoption plan.
**Goal:** Advanced features, repository quality, governance, and a 90-day adoption roadmap.
**Prerequisite:** Completed Path 3 or equivalent experience.
**Time commitment:** ~7 hours.

```
Module 08: Advanced Features
    └── Lab 09: Advanced Feature Tour
Module 09: Repository Quality for AI
    └── Lab 10: Repository Health Audit
Module 10: Adoption Roadmap
    └── Capstone: /capstone/
```

---

## Persona-Based Shortcuts

### "I just want to write better prompts fast"

→ Skip to [Module 04: Prompt Engineering](./modules/04-prompt-engineering/) and the [prompts/](./prompts/) library.

---

### "I'm setting up Copilot for my team"

→ Start with [Module 02: Configuration](./modules/02-configuration/), then [Module 05: Custom Instructions](./modules/05-custom-instructions/), then [Module 10: Adoption Roadmap](./modules/10-adoption-roadmap/).

---

### "I want to review AI-generated code responsibly"

→ [Module 01: Foundations](./modules/01-foundations/) (evaluation section) → [checklists/ai-output-review.md](./checklists/ai-output-review.md) → [agents/code-reviewer.md](./agents/code-reviewer.md)

---

### "I want to understand costs before committing"

→ [Module 03: Token Optimization](./modules/03-token-optimization/) — then read [Module 01](./modules/01-foundations/) for mode selection context.

---

## Full Module Dependency Map

```
01-foundations ──────────────────────────────────────┐
      │                                               │
02-configuration                                      │
      │                                               │
03-token-optimization                              (all paths
      │                                            converge here)
04-prompt-engineering                                 │
      │                                               │
05-custom-instructions                                │
      │                                               ▼
06-agents ──────────────────────────────► 10-adoption-roadmap
      │                                               ▲
07-multi-agent-workflows                              │
      │                                               │
08-advanced-features ── 09-repository-quality ────────┘
```

For the full topic breakdown, see [SYLLABUS.md](./SYLLABUS.md).
