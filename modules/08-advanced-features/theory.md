# Module 08: Advanced Features in Copilot + VS Code — Theory Reference

> Extended reference for [README.md](./README.md). Read the module overview first.
> Prose sections are capped at 500 words; tables and code blocks are excluded from that limit.

---

## Plan Mode Internals

Plan mode differs from Agent mode in two structural ways: it does not execute tool calls, and its output is a text response in the chat panel rather than applied changes. This makes it lower cost and fully reversible. The absence of tool calls means Plan mode cannot read files dynamically during the session — it works from files open in the editor and the conversation context. Files must be explicitly included (via `@workspace` or open editor tabs) before invoking Plan mode.

**Silent failure** is the most common Plan mode problem. Plan mode can return a plausible-looking output that does not address the actual task when the context is ambiguous or when the request contains technical terms the model interprets incorrectly. Detection signals:

- The restatement uses different terminology than the request ("authentication" when the request said "authorization").
- The proposed change references a function that does not exist in the named file.
- The files-to-modify list includes files not mentioned in the request, without explaining why.

When any signal appears, do not proceed to implementation. Clarify the context and re-run Plan mode.

**Plan vs. Agent Planner — the decision rule:** Use Plan mode when the design task is bounded to one session and produces no artifact that another role needs to consume by path. Use an Agent Planner session when the output must be committed as a workflow artifact that the Implementer will reference by file path. Plan mode output is ephemeral — it lives in the chat history. A Planner session artifact is a committed file.

---

## Edits-Style Workflows in Agent Mode (and Custom Agents)

> **Heads up — terminology changed.** A separate **Edit mode** panel existed in earlier VS Code versions and was consolidated into Agent mode in **VS Code 1.110**. Older course materials, screenshots, and team docs that show three panel modes (Ask / Edit / Agent) are out of date. The capability — curated working set + multi-file diff + per-file accept — still exists; it just lives inside Agent mode now, and is generalized further by **custom agents**.

### The current panel-mode set

| Mode | Where it lives | What it does |
|------|---------------|--------------|
| Inline completion | Editor (ghost text) | Continues your typing |
| Inline chat | Editor (`Ctrl+I`) | Single-file targeted change |
| Ask | Chat panel | Conversational answers, no file changes |
| Plan | Chat panel | Proposal output, no tool calls |
| Agent | Chat panel | Reads, writes, runs tools — multi-step |

Edit mode can be temporarily restored via `chat.editMode.hidden: false` but is on a removal trajectory; do not build new workflows on it.

### Doing "Edits-style" work in Agent mode

The discipline that used to live in Edit mode transfers cleanly into Agent mode if you scope the session deliberately:

1. **Name the working set explicitly.** Use `#file:` references for every file the change must touch. Resist `#codebase` for known-scope edits.
2. **Disable terminal in the prompt.** State: *"Do not run terminal commands. Do not run tests. Produce a diff only."*
3. **Forbid out-of-scope edits.** State: *"Edit only the files I named. Do not create new files."*
4. **Review per file.** When the diff arrives, accept or reject each file independently. Do not "Accept all" without per-file review.
5. **One objective per session.** If you find yourself adding a second goal mid-flow, close the session and open a new one.

This recreates the Edit-mode contract: bounded multi-file diff, per-file review, no autonomous tool execution.

### Custom agents — the durable replacement

A **custom agent** is a saved persona: instructions, tool permissions, and (optionally) a default model, invokable in Agent mode by `@name`. Where the manual discipline above is per-session, a custom agent encodes the discipline once and reuses it.

**Anatomy** (per the [VS Code custom agents docs](https://code.visualstudio.com/docs/copilot/customization/custom-agents)):

```markdown
---
name: refactor-coordinator
description: Coordinated multi-file refactor — diff only, no terminal
tools: ['codebase', 'editFiles']
model: claude-sonnet
---

You are a refactor coordinator. You produce a multi-file diff that satisfies
the user's refactor request without running terminal commands or tests.

Rules:
  - Edit only files explicitly named in the user's request via `#file:`.
  - Do not create new files unless the user explicitly asks.
  - Produce a diff per file; do not write narrative explanations between files.
  - If you cannot satisfy the request inside the named files, stop and explain why.
```

Saved as `.github/agents/refactor-coordinator.agent.md`, invoked as `@refactor-coordinator`.

### Decision table — Agent (default) vs. Agent + custom agent vs. Inline chat

| Need | Use | Why |
|------|-----|-----|
| Single-file local edit | Inline chat | Fastest; scoped to selection |
| Coordinated change across known files, one-off | Agent (default) with manual discipline | No setup; transfer the 5 rules above |
| Coordinated change across known files, recurring pattern | Custom agent | Discipline encoded once; team reuses |
| Discovery + change ("find where auth happens, then update it") | Agent (default) with `@workspace` | Tools needed for search |
| Multi-step with terminal/tests | Agent (default) | Tools needed for verification |

### Working-set discipline inside Agent mode

- **Pin only files the change must touch.** A working set of 12 tabs is rarely intentional.
- **Avoid `#codebase` for known-scope edits.** It widens the window and burns tokens.
- **Close unrelated tabs** before starting the session; their content otherwise enters context silently.
- **Re-state the working set** after the model's first response if the diff reaches outside it ("As a reminder, edit only `models.py`, `service.py`, `tests.py`").

### Anti-patterns

- **Referencing "Edits mode" in team docs.** It is gone — update onboarding materials.
- **Custom agents for one-off edits.** If you will run it once, just use Agent mode with the discipline rules. Custom agents cost setup; recover the cost only if you reuse them.
- **Leaving terminal access enabled on a refactor agent.** Silent drift — the agent runs tests, decides they reveal a bug, and starts fixing it. Kill the scope creep at the permission level.
- **Accepting a multi-file diff without per-file review.** The "Accept all" button is the single biggest source of post-AI debugging time.
- **Using a custom agent as a substitute for an instruction file.** If the rule is always-on for the repo, it belongs in `.github/copilot-instructions.md` (Module 05), not in a custom agent.

### Migration note for learners with old habits

If you used Edit mode before, the muscle memory transfers: same working set, same per-file review, different entry point. The first three sessions in Agent mode will feel less constrained than Edit mode did — that is by design, and the discipline rules above replace the structural constraint that Edit mode used to enforce automatically.

---

## MCP — Model Context Protocol

The **Model Context Protocol (MCP)** is an open protocol that lets AI tools (including Copilot Agent mode) call external systems through a standardized interface. Where `@workspace` reads your repo and `@terminal` reads your shell, an MCP server can expose any external system — a database, a browser, a ticketing system, a documentation site — as a set of named tools the agent can call.

MCP is model-agnostic. The same MCP server works with Copilot, Claude, Cursor, or any other MCP client. This makes MCP the durable extensibility surface for Copilot — investments in MCP servers outlast individual product features.

### Why MCP matters for Copilot

Before MCP, extending Agent mode's reach meant either:

- Pasting external data into chat (manual, lossy, expensive in context).
- Using `@terminal` to shell out (fragile, requires re-parsing stdout).
- Building a custom VS Code extension (high effort).

MCP replaces all three for many use cases. An agent can call a typed tool (e.g., `database.query(sql)`) and receive structured results, without parsing free-form text. The discipline rules for `@terminal` (the 4-question gate) apply equally to MCP tool calls.

### Anatomy of an MCP server

| Field | Meaning |
|-------|---------|
| `name` | Unique identifier referenced from `mcp.json` |
| `transport` | How the client talks to the server: `stdio` (subprocess), `sse` (HTTP server-sent events), `http` |
| `command` / `url` | Subprocess command for stdio; URL for sse/http |
| `tools` | Functions the server exposes (declared by the server itself) |
| `permissions` | What the agent is allowed to do with each tool (read-only, write, network) |

### Configuring MCP in VS Code

Workspace-scope: `.vscode/mcp.json`. User-scope: VS Code's user settings.

```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "${workspaceFolder}/scratch"
      ],
      "transport": "stdio"
    }
  }
}
```

After saving, restart the chat session. Tools surface in Agent mode under the server name; the agent picks them when relevant or you can reference them directly in the prompt.

### Decision table — MCP vs. custom agent vs. instruction file vs. prompt file

| Need | Use | Why |
|------|-----|-----|
| Reach an external system (DB, browser, ticketing) | **MCP server** | Standardized protocol; server can be reused across clients |
| Reusable role with bounded tool permissions inside the IDE | **Custom agent** (Module 06/08) | Agent-side persona; does not add new tools |
| Always-on conventions for code generation | **Instruction file** (Module 05) | Passive context, every turn |
| Reusable named action invokable from chat | **Prompt file** (Module 04) | Active, on-demand, parameterized |

A custom agent and an MCP server can — and often should — be combined: the custom agent declares which MCP tools it may use, the MCP server provides the tools.

### Anti-patterns

- **Adding MCP servers "just in case."** Each server is more attack surface and more context noise. Add one when you have a specific failure of `@workspace` / `@terminal` to solve.
- **Granting filesystem-write to untrusted servers.** An MCP server with write access can modify any file in scope. Treat MCP server installation like installing a VS Code extension — verify the source.
- **Chaining MCP tools without bounded scope.** An agent that can call browse → query → write can produce a 30-step session. Restrict tools per agent (custom agent + MCP combo) rather than enabling everything.
- **Trusting MCP output as authoritative.** A `database.query` result is data; a `browser.fetch` result is content. The agent's interpretation is still probabilistic. Verify findings the same way you verify any AI claim.
- **Scoping `server-filesystem` to repo root.** Limit it to a sub-directory (`scratch/`, `data/`, etc.). Repo-root access exposes `.env`, `.git`, and credentials.

### One end-to-end example

**Goal:** Let an agent read and write files inside a sandbox directory using the official `@modelcontextprotocol/server-filesystem` server.

1. **Create the sandbox.** `mkdir scratch` at the repo root. Put two files there: `notes.txt`, `todos.txt`.
2. **Add `.vscode/mcp.json`** with the JSON above (scope: `${workspaceFolder}/scratch`).
3. **Restart the chat session.** Open Agent mode. The `filesystem` server's tools (`read_file`, `write_file`, `list_directory`) should be available.
4. **Run a tool call.** Ask: *"Using the filesystem MCP server, list files in the scratch directory and show me the first 5 lines of each."*
5. **Verify the trace.** Inspect the tool call in the chat output — server name, tool name, arguments, result. This is the JSON-RPC contract that makes MCP debuggable.
6. **Test the boundary.** Ask the agent to read `package.json` (outside the scratch scope). The server should refuse. If it does not, your scope is mis-configured.

> **Verify before assuming.** MCP spec, server names, transport modes, and VS Code's MCP UI all evolve. Pin a verified date in any team docs that reference specific config syntax. Authoritative sources: [Model Context Protocol spec](https://modelcontextprotocol.io/), [VS Code MCP docs](https://code.visualstudio.com/docs/copilot/mcp).

---

## CI/CD Integration Patterns

Four integration points span the full CI/CD lifecycle. Each has a distinct risk profile.

| Integration point | Copilot output | Review gate |
|-------------------|----------------|------------|
| PR title and description | Prose summary of the diff | One human reads and approves before merge |
| Inline review comment | Code suggestion on a specific diff line | Same triage gate as a Code Reviewer session finding |
| Pipeline step suggestion | A YAML block or shell command | 4-question gate before adding to the pipeline definition |
| Failure explanation | Prose: what failed and why | Read only — no code change generated from this output |

The failure explanation integration is the safest and most immediately valuable: paste a CI failure log into chat and ask Copilot to explain it before reading the stack trace manually. This adds no code risk and saves significant diagnosis time.

Copilot does not replace human code ownership in CI/CD. Every AI-assisted commit that merges needs a named human reviewer on record. An automated pipeline that accepts AI output without a human gate is an unmonitored code path — treat it as a critical security gap.

---

## Enterprise Context Management

For teams on Copilot Business or Copilot Enterprise, context controls extend beyond `.copilotignore`.

| Control | Scope | Set by |
|---------|-------|--------|
| `.copilotignore` | Repository — files excluded from context in this repo | Developer |
| Content exclusions (admin console) | Organization — patterns excluded across all repos | Admin |
| Knowledge base (Enterprise only) | Organization — custom documentation indexed for chat | Admin |
| Data residency settings | Plan-level — where prompt data is processed | Account admin |

For codebases in scope for SOC 2, PCI-DSS, or HIPAA, confirm data residency and organizational content exclusion settings with the account administrator before using Copilot on in-scope files. A `.copilotignore` file alone does not satisfy compliance requirements — organizational controls must be set at the admin level.

For large teams, treat `.copilotignore` changes the same as changes to security configuration. Create a shared template in the repository and require that removal of any exclusion entry passes the same review process as a change to authentication logic. Entries do not expire and do not self-update — audit the file whenever the sensitive-file inventory changes.

---

## Workflow File vs. Plan Mode Output

Module 07 introduced the workflow file (`agents/workflow-*.md`) as the artifact that coordinates multi-agent sessions. Plan mode output is distinct:

| Artifact | Lives in | Consumed by | Persists? |
|----------|---------|-------------|-----------|
| Workflow file | `agents/` — committed to repo | All sessions in the workflow by path | Yes — survives session boundaries |
| Plan mode output | Chat history | Current session only | No — lost when chat is closed |
| Code Reviewer findings | Committed markdown | Human reviewer; next session via handoff | Yes — if explicitly committed |

The implication: when Plan mode produces a design that will be consumed by a subsequent Implementer session, commit it before closing the tab. Use the workflow file pattern from Module 07 rather than copying from chat history.

---

## Official Resources

- [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
- [Use chat in VS Code](https://code.visualstudio.com/docs/copilot/copilot-chat)
- [Copilot customization in VS Code](https://code.visualstudio.com/docs/copilot/copilot-customization)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)

---

← [Back to Module 08 README](./README.md)
