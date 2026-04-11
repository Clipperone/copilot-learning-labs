# Module 08: Advanced Features in Copilot + VS Code — Theory

This document extends the README with technical reference material. Read the README first — this file assumes that content.

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
