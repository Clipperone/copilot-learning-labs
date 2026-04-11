# Learning Path

## GitHub Copilot Pro+ Mastery in VS Code

Choose the path that matches where you are today, not where you want to be. Dependencies are strict: each level builds on the previous one. The shortcuts at the bottom are for learners who have genuine prior experience.

For the full topic-by-topic breakdown, see [SYLLABUS.md](./SYLLABUS.md).

---

## Where Do I Start?

Answer these questions to self-place:

| Question | If yes → |
|----------|---------|
| I have not used GitHub Copilot before | **Start at Path 1** |
| Copilot is installed but I mostly use ghost text and basic chat | **Start at Path 1** — complete it and move to Path 2 |
| I write structured prompts deliberately and have a configured project | **Start at Path 2** |
| I have working custom instructions and a personal prompt library | **Start at Path 3** |
| I run agent sessions and multi-agent workflows regularly | **Start at Path 4** |

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

```
Module 01: Foundations                          ~2 hrs
    └── Lab 01: Getting Started                 ~40 min
Module 02: Configuration                        ~2 hrs
    └── Lab 02: Project Configuration Baseline  ~50 min
Module 03: Token Optimization                   ~1.5 hrs
    └── Lab 03: Token Audit Exercise            ~35 min
    └── checklists/beginner-completion.md  ← self-assess before advancing
```

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

```
Module 04: Prompt Engineering                   ~2.5 hrs
    └── Lab 04: Prompt Engineering Workshop        ~50 min
Module 05: Custom Instructions                  ~2 hrs
    └── Lab 05: Write Your Project's Custom Instructions  ~50 min
    └── checklists/intermediate-completion.md  ← self-assess before advancing
```

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

```
Module 06: Agents and Role Specialization       ~3 hrs
    └── Lab 07: Define and Run Your First Agent Session  ~60 min
Module 07: Multi-Agent Workflows                ~2.5 hrs
    └── Lab 08: Run a Complete Multi-Agent Workflow      ~60 min
    └── checklists/advanced-completion.md  ← self-assess before advancing
```

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

```
Module 08: Advanced Features                    ~2.5 hrs
    └── Lab 09: Advanced Feature Tour           ~50 min
Module 09: Repository Quality for AI            ~2 hrs
    └── Lab 10: Repository Health Audit         ~60 min
Module 10: Adoption Roadmap                     ~2 hrs
    └── Capstone: /capstone/
    └── checklists/expert-completion.md  ← final self-assessment
```

**Exit deliverables:**
- Capstone project complete and self-assessed
- Written 90-day adoption roadmap
- `checklists/expert-completion.md` fully checked

---

## Persona-Based Shortcut Paths

Use these only if you have genuine prior experience with the skills they skip. If in doubt, take the full path.

### "I want to write better prompts immediately"

Prerequisite: Copilot is installed and running.

```
Module 03: Token Optimization  (compact prompt section only)
    ↓
Module 04: Prompt Engineering
    └── Lab 04: Prompt Patterns Workshop
    └── Lab 05: Build a Personal Prompt Library
```

Then return to Module 01 to fill any gaps.

---

### "I'm configuring Copilot for my team"

Prerequisite: Copilot Pro+ is deployed. You have admin access.

```
Module 02: Configuration
    └── Lab 02: Project Configuration Baseline
Module 05: Custom Instructions
    └── Lab 06: Write Your Project's Custom Instructions
Module 10: Adoption Roadmap (team section)
```

---

### "I want to review AI-generated code responsibly"

Prerequisite: None.

```
Module 01: Foundations (critical evaluation section)
    └── checklists/ai-output-review.md
    └── checklists/pre-commit.md
Module 09: Repository Quality for AI (governance section)
    └── agents/code-reviewer.md  (Path 3 required)
```

---

### "I want to understand costs before committing"

Prerequisite: None — this is a good first read.

```
Module 03: Token and Premium Request Optimization
    └── Lab 03: Token Audit Exercise
```

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
