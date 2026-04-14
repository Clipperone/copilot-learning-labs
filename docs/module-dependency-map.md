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
                                          11-platform-integration
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
| Lab 06 — Agents and Personas | Module 06 | Lab 05 |
| Lab 07 — Run a Complete Multi-Agent Workflow | Module 07 | Lab 06 |
| Lab 08 — Advanced Feature Tour | Module 08 | Lab 07 |
| Lab 09 — Repository Health Audit | Module 09 | none (standalone) |
| Module 11 — Platform & GitHub.com Integration | Module 11 (in-module exercises only — no separate lab; coding-agent / github.com / CLI work happens outside a local repo, so a lab folder would be artificial) | Module 10 |
| Capstone — End-to-End Copilot Workflow Integration | Module 11 | Labs 01–09 + Module 11 in-module exercises |

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
| `.vscode/mcp.json` (example) | Module 08 |
| `.github/prompts/*.prompt.md` | Module 04 |
| `.github/agents/*.agent.md` (custom agents) | Module 08 |
| `.github/copilot-setup-steps.yml` | Module 11 |
| `capstone/` | Module 10 (D1–D7) + Module 11 (D8) |

---

## Shortcut Paths (no-prerequisite entry points)

| If you want to… | Jump to |
|----------------|---------|
| Just get the AI output review checklist | `checklists/ai-output-review.md` |
| Copy a custom instruction example immediately | `instructions/` |
| Use a prompt right now | `prompts/generation/generate-function.md` |
| Understand agent mode without the full course | `agents/README.md` |

These are useful for experienced practitioners. For learners, follow the linear chain above.
