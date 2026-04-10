# Module 01: Foundations — Extended Theory

> Reference material to supplement the module README. Read this for deeper context or when the README summary is insufficient.

---

## GitHub Copilot Pro+ vs. Other Plans

| Feature | Free | Pro | Pro+ | Business | Enterprise |
|---------|------|-----|------|----------|------------|
| Inline completion | ✅ | ✅ | ✅ | ✅ | ✅ |
| Chat (included model) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Premium model access | ❌ | Limited | ✅ | ✅ | ✅ |
| Agent mode | ❌ | ❌ | ✅ | ✅ | ✅ |
| Premium request quota | — | — | Monthly allotment | Seat-based | Seat-based |

> Plan features change frequently. Verify at [https://github.com/features/copilot](https://github.com/features/copilot).

---

## How GitHub Copilot Works (Operational Model)

Copilot sends a **prompt** to a language model and returns a **completion**. The prompt includes:

- The text you typed (or the chat message you sent)
- Surrounding file context (content before and after your cursor)
- Open tabs and referenced files (depending on mode)
- Custom instructions (if configured)
- Conversation history (in chat modes)

The model does not have access to your file system beyond what VS Code passes in the context window. It does not remember previous sessions.

### What "context window" means in practice

The context window is the maximum amount of text the model can process in a single request. Anything outside the window is invisible. For large files or long conversations:

- Earlier parts of the conversation may be dropped
- Files you haven't opened may not be included
- Large files may be truncated

This is why context management matters — covered in Module 03.

---

## The Inline Completion Model (Ghost Text)

Inline completions are generated as you pause typing. VS Code sends:

- Content before the cursor (primary signal)
- Content after the cursor (used for "fill in the middle" completions)
- File type and language hint

**Key behaviors:**
- `Tab` — accept full suggestion
- `Ctrl+Right` (Windows/Linux) / `Option+Right` (Mac) — accept one word at a time
- `Esc` — dismiss
- `Alt+]` / `Alt+[` — cycle through alternative suggestions

---

## Chat Mode Architecture

In chat modes (ask, edit, plan, agent), Copilot operates as a **conversation** with tool access:

| Mode | Tool access | File edits | Multi-step |
|------|-------------|-----------|-----------|
| Ask | Read-only reference | No | No |
| Edit | Current file(s) | Yes, direct | No |
| Plan | Read-only | No | No (plans only) |
| Agent | Read, write, terminal, search | Yes | Yes |

**Agent mode** is the most powerful but also the most expensive in terms of premium requests. It can loop through multiple steps, run commands, read and write files, and use web search if configured.

---

## Why Critical Evaluation Matters

Language models are trained to produce **plausible text**, not necessarily correct code. Common failure modes:

| Failure type | Example | Detection strategy |
|-------------|---------|-------------------|
| Hallucinated API | Calls `list.findLast()` in Python 3.8 which doesn't exist | Check API docs; run the code |
| Correct pattern, wrong context | Adds `async/await` where the framework is synchronous | Understand the context before accepting |
| Missing error handling | Happy-path only; exceptions will crash | Ask Copilot: "What can go wrong here?" |
| Security anti-pattern | Concatenates user input into SQL | Use security review prompt; check OWASP |
| Stale knowledge | References a deprecated API | Search current docs for the symbol |

The four critical questions from the module README are the minimum gate. For production code, use the [AI output review checklist](../../checklists/ai-output-review.md).

---

## Official Resources

- [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [GitHub Copilot feature comparison](https://docs.github.com/en/copilot/about-github-copilot/subscription-plans-for-github-copilot)
- [VS Code Copilot keyboard shortcuts](https://code.visualstudio.com/docs/copilot/copilot-vscode-features)
