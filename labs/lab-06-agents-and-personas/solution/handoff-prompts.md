# Reference Handoff Prompts

Three standard handoff prompts for the most common role transitions. Use these as structural references when writing your own handoff prompts in Task 3. The specific content (file paths, task names, acceptance criteria) must come from your own session — adapt the structure, not the content.

---

## 1. Planner → Implementer

**When to use:** The Planner has produced a task breakdown and the first sub-task is ready to execute.

**Handoff prompt:**

```
Summary: The Planner produced a task breakdown for the notification system feature in
feature-plan.md. This session covers sub-task 1: Implement log_event() in notifications.py.
Acceptance criterion: log_event() raises ValueError for invalid event types and calls the
stdlib logger with level INFO for valid events. Affected file: starter/notifications.py.

Objective: Implement sub-task 1 only. Do not proceed to sub-task 2 or write tests in this session.

Carry-forward:
- Active instruction file: .github/copilot-instructions.md
- Do not modify any file other than starter/notifications.py
- Do not change the function signature defined in the starter file
- Exit condition: log_event() raises ValueError for invalid event_type and logs at INFO
  for each of the three valid event types. All pre-existing tests pass.
```

---

## 2. Implementer → Code Reviewer

**When to use:** The Implementer has completed a sub-task, all tests pass, and the change is ready for review before commit.

**Handoff prompt:**

```
Summary: The Implementer implemented sub-task 1 — log_event() in starter/notifications.py.
The function validates event_type against VALID_EVENT_TYPES, raises ValueError for invalid
types, and logs at INFO with the format "event_type=X user_id=Y". All 4 tests pass.

Objective: Review the changes to starter/notifications.py for correctness, style, and
edge-case handling. Do not review any other file.

Carry-forward:
- Active instruction file: .github/copilot-instructions.md
- Do not edit any file — produce a findings document only
- Categorize each finding as Blocking (must fix before commit) or Advisory
- Exit condition: Findings document complete with blocking/advisory categorization.
  Zero blocking issues means the change is ready to commit.
```

---

## 3. Code Reviewer → Security Reviewer

**When to use:** The Code Reviewer has completed a review and identified code that processes external input or writes to a log that may contain sensitive data.

**Handoff prompt:**

```
Summary: Code review of starter/notifications.py found 0 blocking issues and 2 advisory
issues (see code-review-findings.md). The implementation logs user_id directly in the log
message — the Code Reviewer flagged this for security analysis.

Objective: Analyze starter/notifications.py for OWASP Top 10 vulnerabilities.
Specifically: does logging user_id in the event log create a data exposure risk (OWASP A02)?
Does the ValueError path leak any implementation details through exception messages?

Carry-forward:
- Active instruction file: .github/copilot-instructions.md
- Do not edit any file — produce a security findings document only
- Classify findings as Critical, High, Medium, or Informational with OWASP category
- Exit condition: Security findings document complete.
  Any Critical or High finding must be resolved before the implementation is committed.
```

---

## What Makes a Good Handoff Prompt

Every handoff prompt must have exactly three parts:

| Part | Purpose | What to include |
|------|---------|----------------|
| **Summary** | Describes what the previous role produced | Filename, what was done, key facts (test count, acceptance criterion met) |
| **Objective** | Scopes the next session's work | Single bounded task, specific file path, what to produce |
| **Carry-forward** | Preserves project context across session boundary | Active instruction file path, explicit exclusions, exact exit condition |

The Carry-forward block is the most commonly omitted part. Without it, the next session starts without the project's active instruction rules.
