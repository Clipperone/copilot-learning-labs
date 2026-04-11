# Module Dependency Map

This document shows which modules depend on which, and in what order the full course should be followed.

---

## Linear Dependency Chain

```
01-foundations
    │
    └──► 02-configuration
              │
              └──► 03-token-optimization
                        │
                        └──► 04-prompt-engineering
                                  │
                                  └──► 05-custom-instructions
                                            │
                                            └──► 06-agents
                                                      │
                                                      └──► 07-multi-agent-workflows
                                                                │
                                                    ┌───────────┘
                                                    │
                                          08-advanced-features
                                                    │
                                          09-repository-quality
                                                    │
                                          10-adoption-roadmap
                                                    │
                                               capstone/
```

Each module assumes completion of all modules before it in this chain.

---

## Lab-to-Module Map

| Lab | Primary module | Secondary dependencies |
|-----|---------------|----------------------|
| Lab 01 — Setup and Verify | Module 01 | none |
| Lab 02 — Project Configuration | Module 02 | Lab 01 |
| Lab 03 — Token Audit | Module 03 | Lab 01 |
| Lab 04 — Prompt Engineering Workshop | Module 04 | Lab 01 |
| Lab 05 — Custom Instructions | Module 05 | Lab 04 |
| Lab 07 — First Agent Session | Module 06 | Lab 06 |
| Lab 08 — Multi-Agent Workflow | Module 07 | Lab 07 |
| Lab 09 — Advanced Feature Tour | Module 08 | Lab 07 |
| Lab 10 — Repository Health Audit | Module 09 | none (standalone) |

---

## Asset-to-Module Map

| Asset / folder | First used in module |
|---------------|---------------------|
| `prompts/` | Module 04 |
| `instructions/` | Module 05 |
| `agents/` | Module 06 |
| `checklists/ai-output-review.md` | Module 01 |
| `checklists/pre-commit.md` | Module 02 |
| `checklists/adoption-milestones.md` | Module 10 |
| `capstone/` | Module 10 |
| `examples/` | Module 07 |

---

## Shortcut Paths (no-prerequisite entry points)

| If you want to… | Jump to |
|----------------|---------|
| Just get the AI output review checklist | `checklists/ai-output-review.md` |
| Copy a custom instruction example immediately | `instructions/` *(v0.3)* |
| Use a prompt right now | `prompts/generation/generate-function.md` |
| Understand agent mode without the full course | `agents/README.md` *(v0.4)* |

These are useful for experienced practitioners. For learners, follow the linear chain above.
