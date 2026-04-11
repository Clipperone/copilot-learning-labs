# Module 02: Configuration — Completion Checklist

Use this checklist to self-assess before moving to Module 03.

---

## VS Code Settings

- [ ] `.vscode/settings.json` exists in the project and is committed to the repository
- [ ] `github.copilot.chat.codeGeneration.useInstructionFiles` is set to `true`
- [ ] `editor.formatOnSave` is enabled
- [ ] `files.exclude` hides `__pycache__`, `node_modules`, or other build artifacts

---

## Copilot Instructions

- [ ] `.github/copilot-instructions.md` exists in the project
- [ ] The file contains at least 3 specific, verifiable coding conventions
- [ ] I verified Copilot reads the instructions by asking "What are your coding conventions for this project?"
- [ ] Instructions use imperative form ("Use `snake_case`…") not descriptive form ("The project uses…")

---

## File Organization

- [ ] I can explain why large utility files degrade Copilot suggestion quality
- [ ] Each source file in my project has a single clear responsibility
- [ ] File and folder names are descriptive — a new developer (or Copilot) can infer the content from the name

---

## Linting and Formatting

- [ ] A linter runs on save in VS Code (Ruff, ESLint, or equivalent)
- [ ] A formatter is configured and formats consistently on save
- [ ] `.editorconfig` exists and defines baseline whitespace settings

---

## Task Automation

- [ ] `.vscode/tasks.json` defines a `test` task
- [ ] The task runs successfully via **Terminal → Run Task**
- [ ] I tested invoking the task from agent mode

---

## Exercise Completion

- [ ] Exercise 1 completed — wrote project-level Copilot instructions and verified they are read
- [ ] Exercise 2 completed — tested instruction effectiveness with a code generation prompt
- [ ] Exercise 3 completed — audited a file for context dilution
- [ ] Exercise 4 completed — linter configured and running on save
- [ ] Exercise 5 completed — defined a task and invoked it via agent mode
- [ ] Exercise 6 completed — created `.vscode/extensions.json` with recommendations
- [ ] Exercise 7 completed — compared Copilot suggestion quality before and after type annotations

---

## Ready for Module 03?

Complete all sections above, then move to the next module.

- [ ] [Lab 02](../../labs/lab-02-configuration/) completed (all 6 tasks)
- [ ] All 7 exercises complete

→ [Module 03: Token and Premium Request Optimization](../03-token-optimization/)
