# Learning Path

## GitHub Copilot Pro+ Mastery in VS Code

Choose the path that matches where you are today, not where you want to be. Dependencies are strict: each level builds on the previous one. The shortcuts at the bottom are for learners who have genuine prior experience.

For the full topic-by-topic breakdown, see [SYLLABUS.md](./SYLLABUS.md).

---

## Where Do I Start?

Answer these questions to self-place:

| Question | If yes → |
|----------|---------|
| Copilot is installed but I mostly use ghost text and basic chat | [**Start at Path 1**](#path-1--beginner) |
| I write structured prompts deliberately and have a configured project | [**Start at Path 2**](#path-2--intermediate) |
| I have working custom instructions and a personal prompt library | [**Start at Path 3**](#path-3--advanced) |
| I run agent sessions and multi-agent workflows regularly | [**Start at Path 4**](#path-4--expert) |

---

## Path 1 — Beginner

**You:** New to Copilot, or using it passively (ghost text + occasional chat) without deliberate technique.

**You will be able to, after this path:**
- Use all six Copilot modes correctly and choose the right one for each task
- Configure any project with a working instruction file, linter, and task runner
- Make cost-aware decisions between included and premium requests without looking them up
- Evaluate AI-generated code with the four-question review gate before every commit

**Prerequisites:** GitHub account with Copilot subscription. VS Code installed. No Copilot experience required.

**Time commitment:** ~6 hours

**Entry gate:** None.

| Step | What | Time |
|------|------|------|
| 1 | [Module 01 — Foundations](./modules/01-foundations/) | ~2 hrs |
| 2 | [Lab 01 — Getting Started](./labs/lab-01-getting-started/) | ~40 min |
| 3 | [Module 02 — Configuration](./modules/02-configuration/) | ~2 hrs |
| 4 | [Lab 02 — Project Configuration Baseline](./labs/lab-02-configuration/) | ~50 min |
| 5 | [Module 03 — Token Optimization](./modules/03-token-optimization/) | ~1.5 hrs |
| 6 | [Lab 03 — Token Audit Exercise](./labs/lab-03-token-audit/) | ~35 min |
| 7 | [beginner-completion.md](./checklists/beginner-completion.md) ← self-assess before advancing | — |

**Exit deliverables:**
- Working Copilot Pro+ setup verified across all modes
- `.github/copilot-instructions.md` with 3+ specific rules on a real project
- Personal mode/model decision cheat sheet

**Next:** → [Path 2 — Intermediate](#path-2--intermediate)

---

## Path 2 — Intermediate

**You:** Copilot works. You use it regularly. You want to stop relying on follow-up turns and start getting complete, correct results on the first try.

**You will be able to, after this path:**
- Write a complete, structured prompt for any coding scenario — generation, refactoring, debugging, testing, documentation, security — without follow-ups
- Recognize the five prompt anti-patterns and fix them on sight
- Maintain persistent custom instructions at global, repository, and path scope
- Operate a personal prompt library of 5+ reusable, tested prompts committed to `prompts/`

**Prerequisites:** Path 1 complete. Copilot is running in a configured project with an instruction file.

**Time commitment:** ~5 hours

**Entry gate:** [checklists/beginner-completion.md](./checklists/beginner-completion.md) fully checked.

| Step | What | Time |
|------|------|------|
| 1 | [Module 04 — Prompt Engineering](./modules/04-prompt-engineering/) | ~2.5 hrs |
| 2 | [Lab 04 — Prompt Engineering Workshop](./labs/lab-04-prompt-engineering/) | ~50 min |
| 3 | [Module 05 — Custom Instructions](./modules/05-custom-instructions/) | ~2 hrs |
| 4 | [Lab 05 — Write Your Project's Custom Instructions](./labs/lab-05-custom-instructions/) | ~50 min |
| 5 | [intermediate-completion.md](./checklists/intermediate-completion.md) ← self-assess before advancing | — |

**Exit deliverables:**
- 5 prompt entries committed to `prompts/` using the course template
- `instructions/` folder with 3 scoped examples (global, project, path-specific)

**Next:** → [Path 3 — Advanced](#path-3--advanced)

---

## Path 3 — Advanced

**You:** Structured prompting is a consistent habit. You have working custom instructions. You want to delegate complex tasks to specialized agents and coordinate them across sessions.

**You will be able to, after this path:**
- Define a role-specialized agent persona with explicit tool permissions and a handoff protocol
- Run a single-agent session with a scoped objective and a defined exit condition
- Decompose a complex task into a multi-agent workflow and execute it without context pollution
- Know when to stop an agent, when to hand off, and when to start a new session

**Prerequisites:** Path 2 complete. A working prompt library and instruction files are in place.

**Time commitment:** ~6 hours

**Entry gate:** [checklists/intermediate-completion.md](./checklists/intermediate-completion.md) fully checked.

| Step | What | Time |
|------|------|------|
| 1 | [Module 06 — Agents and Role Specialization](./modules/06-agents/) | ~3 hrs |
| 2 | [Lab 06 — Agents and Personas](./labs/lab-06-agents-and-personas/) | ~60 min |
| 3 | [Module 07 — Multi-Agent Workflows](./modules/07-multi-agent-workflows/) | ~2.5 hrs |
| 4 | [Lab 07 — Run a Complete Multi-Agent Workflow](./labs/lab-07-multi-agent-workflow/) | ~70 min |
| 5 | [advanced-completion.md](./checklists/advanced-completion.md) ← self-assess before advancing | — |

**Exit deliverables:**
- All 10 agent definitions in `agents/`
- One documented, repeatable multi-agent workflow file

**Next:** → [Path 4 — Expert](#path-4--expert)

---

## Path 4 — Expert

**You:** Advanced practitioner. You have run agent workflows in real projects. You want to apply the full feature set, harden your practices, and build a plan to scale this to a team.

**You will be able to, after this path:**
- Apply Plan mode, AI review, terminal integration, and CI/CD features with deliberate intent
- Audit any repository for AI-friendliness and fix the problems you find
- Govern AI-generated code with a documented review protocol applied before every commit
- Write and execute a personal or team 90-day Copilot adoption roadmap

**Prerequisites:** Path 3 complete. Multi-agent workflows have been run at least once.

**Time commitment:** ~7 hours

**Entry gate:** [checklists/advanced-completion.md](./checklists/advanced-completion.md) fully checked.

| Step | What | Time |
|------|------|------|
| 1 | [Module 08 — Advanced Features](./modules/08-advanced-features/) | ~2.5 hrs |
| 2 | [Lab 08 — Advanced Feature Tour](./labs/lab-08-advanced-feature-tour/) | ~60 min |
| 3 | [Module 09 — AI-Friendly Repository Engineering](./modules/09-repository-quality/) | ~2 hrs |
| 4 | [Lab 09 — Repository Health Audit](./labs/lab-09-repository-health-audit/) | ~60 min |
| 5 | [Module 10 — Adoption Roadmap](./modules/10-adoption-roadmap/) | ~2 hrs |
| 6 | [Capstone — End-to-End Copilot Workflow Integration](./capstone/) | ~2 hrs |
| 7 | [expert-completion.md](./checklists/expert-completion.md) ← final self-assessment | — |

**Exit deliverables:**
- 7 capstone deliverables committed (instructions, conventions, agents, prompts, workflow, validation report, roadmap)
- Written 90-day adoption roadmap
- [checklists/expert-completion.md](./checklists/expert-completion.md) fully checked

---

## Persona-Based Shortcut Paths

Use these only if you have genuine prior experience with the skills they skip. If in doubt, take the full path.

### "I want to write better prompts immediately"

Prerequisite: Copilot is installed and running.

1. [Module 03 — Token Optimization](./modules/03-token-optimization/) (compact prompt section only)
2. [Module 04 — Prompt Engineering](./modules/04-prompt-engineering/)
3. [Lab 04 — Prompt Engineering Workshop](./labs/lab-04-prompt-engineering/)

Then return to Module 01 to fill any gaps.

---

### "I'm configuring Copilot for my team"

Prerequisite: Copilot Pro+ is deployed. You have admin access.

1. [Module 02 — Configuration](./modules/02-configuration/)
2. [Lab 02 — Project Configuration Baseline](./labs/lab-02-configuration/)
3. [Module 05 — Custom Instructions](./modules/05-custom-instructions/)
4. [Lab 05 — Write Your Project's Custom Instructions](./labs/lab-05-custom-instructions/)
5. [Module 10 — Adoption Roadmap](./modules/10-adoption-roadmap/) (team section)

---

### "I want to review AI-generated code responsibly"

Prerequisite: None.

1. [Module 01 — Foundations](./modules/01-foundations/) (critical evaluation section)
2. [checklists/ai-output-review.md](./checklists/ai-output-review.md)
3. [checklists/pre-commit.md](./checklists/pre-commit.md)
4. [Module 09 — AI-Friendly Repository Engineering](./modules/09-repository-quality/) (governance section)
5. [agents/code-reviewer.md](./agents/code-reviewer.md) (Path 3 required)

---

### "I want to understand costs before committing"

Prerequisite: None — this is a good first read.

1. [Module 03 — Token Optimization](./modules/03-token-optimization/)
2. [Lab 03 — Token Audit Exercise](./labs/lab-03-token-audit/)

Then start Path 1 from the beginning.

---

## Full Module Dependency Map

```
01-foundations
      |
02-configuration
      |
03-token-optimization
      |
04-prompt-engineering
      |
05-custom-instructions
      |
06-agents
      |
07-multi-agent-workflows
      |
08-advanced-features
      |
09-repository-quality
      |
10-adoption-roadmap
      |
  Capstone
```

Every module depends on all modules above it. There are no optional detours, no parallel tracks, and no modules that can be swapped in order.
