# Module 03: Token and Premium Request Optimization — Completion Checklist

Use this checklist to self-assess before moving to Module 04.

---

## Request Type Awareness

- [ ] I can distinguish between included requests and premium requests without looking them up
- [ ] I know which of the following are premium: agent mode, Plan mode with default model, o1, GPT-4o
- [ ] I understand that large context windows increase premium request cost, even with the same model

---

## Mode and Model Selection

- [ ] I default to inline completion for short, ephemeral suggestions
- [ ] I default to Ask (default model) for explanations and questions
- [ ] I use inline chat for single-file targeted changes
- [ ] I reserve agent mode for tasks that require tool use or span multiple files
- [ ] I can justify in one sentence why I would choose a premium model over the default

---

## Prompt Quality

- [ ] My prompts include: goal, constraints, and output format when non-default
- [ ] I can apply the "one noun, one verb" test to any prompt before sending
- [ ] I rewrote at least 3 prompts from Exercise 3 and found them more useful than the originals

---

## Context Hygiene

- [ ] I close irrelevant files before starting a focused agent session
- [ ] I use `#selection` or `#file:` when the target is specific, rather than relying on open tabs
- [ ] I start a new chat session for each distinct task rather than continuing long threads

---

## Context Variables and Chat Participants

- [ ] I can name and use `#file:`, `#selection`, `#codebase`, `#sym`, `#changes`, `#terminalLastCommand`
- [ ] I can name and use `@workspace`, `@terminal`, `@vscode` and state when each is the right participant
- [ ] I default to `#file:` over leaving tabs open, and to `@workspace` over pasting multiple files
- [ ] I treat `#codebase` as a discovery tool, not a default — I use it only when I do not know where the answer lives

---

## Exercise Completion

- [ ] Exercise 1 completed — classified 10 actions correctly
- [ ] Exercise 2 completed — selected appropriate mode/model for 8 task scenarios
- [ ] Exercise 3 completed — rewrote 3 verbose prompts as compact single-turn prompts
- [ ] Exercise 4 completed — ran the context window experiment and documented observations
- [ ] Exercise 5 completed — personal mode/model cheat sheet produced (Lab 03 deliverable)

---

## Ready for Module 04?

Complete all sections above, then move to the next module.

- [ ] [Lab 03](../../labs/lab-03-token-audit/) completed — worksheet filled, personal cheat sheet finalized
- [ ] All 5 exercises complete

→ [Module 04: Prompt Engineering for Coding](../04-prompt-engineering/)
