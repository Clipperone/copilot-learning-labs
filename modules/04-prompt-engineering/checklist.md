# Module 04 — Completion Checklist

Use this checklist after finishing the module and before starting Lab 04. If you cannot check an item confidently, revisit the linked section.

---

## Prompt Architecture

- [ ] I can name the four components of a structured prompt: Task, Role, Constraints, Output format.
- [ ] I can apply the completeness test to a Task line: one verb, one noun.
- [ ] I know which components are required for every prompt and which are conditional.

## Scenario Coverage

- [ ] Code generation: I name the function, types, and constraints — and ask for the function body only.
- [ ] Refactoring: I state what changes and what must not change before writing the prompt.
- [ ] Debugging: I describe symptoms, expected, and actual — and ask for diagnosis before the fix.
- [ ] Testing: I list edge cases explicitly and specify the framework and assertion style.
- [ ] Documentation: I state the audience, the format, and the depth.
- [ ] Code review: I scope to one concern per prompt and state what is out of scope.
- [ ] Security review: I cite the OWASP category and ask for the exploit path before the fix.

## Anti-patterns

- [ ] I can identify a vague-target prompt on sight and rewrite it.
- [ ] I know why double-task prompts produce worse results than two separate prompts.
- [ ] I understand why pasting only an error message is insufficient for a debugging prompt.
- [ ] I know what "missing output format" looks like and how to fix it.
- [ ] I can explain why asking for a fix before diagnosis is a structural mistake.

## Reusable Templates

- [ ] I can convert a working one-off prompt into a parameterized template using `[PLACEHOLDER]` convention.
- [ ] I know the four signs that a prompt is ready to commit to the shared library.
- [ ] I have read [templates/prompt-template.md](../../templates/prompt-template.md).

## Prompt Files (`.prompt.md`)

- [ ] I can name where prompt files live (workspace `.github/prompts/` and user prompts directory).
- [ ] I can write the minimum frontmatter (`mode`, `description`) and add `model` / `tools` only when justified.
- [ ] I can convert `[PLACEHOLDER]` to `${input:variableName}` and use `${selection}` / `${file}` / `${workspaceFolder}` correctly.
- [ ] I can choose between an instruction file (always-on), a prompt file (named action), and a custom agent (scoped role).
- [ ] I completed Exercise 6 — promoted one Markdown prompt to `.prompt.md` and verified two invocations with different inputs.

## Premium Model Decisions

- [ ] I know which scenarios warrant a premium model and can justify the decision.
- [ ] I know that docstrings, refactoring, and test generation do not require premium models.
- [ ] I know that OWASP security review and async debugging are the primary justified cases.

---

## Ready for Lab 04?

All items above checked → proceed to [Lab 04 — Prompt Engineering Workshop](../../labs/lab-04-prompt-engineering/).

Not all items checked → return to [exercises.md](./exercises.md) for the specific scenario you want to reinforce.
