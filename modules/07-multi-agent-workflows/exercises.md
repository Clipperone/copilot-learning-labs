# Module 07: Multi-Agent Workflows — Exercises

Complete these exercises in order. Expected answers are provided after each exercise — work through the problem independently before reading the answer.

---

## Exercise 1 — Decompose for a Workflow

**Type:** Decomposition practice
**Time:** ~15 minutes

**Context:**

You have received the following feature request:

> **Feature: Audit Log**
>
> All write operations in the system must be recorded for compliance purposes.
>
> Requirements:
> - Add a `record_write(resource_type: str, resource_id: str, action: str) -> None` function to `audit_log.py` that appends an entry to an in-memory log.
> - Add a `get_log(resource_type: str) -> list[dict]` function to `audit_log.py` that returns all entries matching the given resource type.
> - Guard `delete_record()` in `records.py` so it calls `record_write()` with `action="delete"` before removing the record.
> - Add at least one test per new function to `tests/test_audit_log.py`.

**Task:**

Produce a valid sub-task breakdown for the Feature Delivery pattern. For each sub-task:
- State the file scope (named files only)
- Write one acceptance criterion
- Confirm the sub-task contains no "and" connecting two separate implementation steps

**Expected answer:**

| Sub-task | File scope | Acceptance criterion |
|----------|-----------|----------------------|
| 1 — Add `record_write()` | `audit_log.py` | Function exists; calling it with valid arguments appends one entry to the in-memory log |
| 2 — Add `get_log()` | `audit_log.py` | Function exists; returns only entries whose `resource_type` matches the argument; returns an empty list when no entries match |
| 3 — Guard `delete_record()` in `records.py` | `records.py` | `delete_record()` calls `record_write()` with `action="delete"` before removing the record; the audit entry is present in the log after the call |
| 4 — Add tests for sub-tasks 1 and 2 | `tests/test_audit_log.py` | At least one test per function; both pass in the test runner |
| 5 — Add tests for sub-task 3 | `tests/test_audit_log.py` | At least one test confirms the audit entry is written before deletion completes |

**Why these boundaries?** Sub-tasks 1 and 2 are separate because they are independent functions with independent acceptance criteria. Sub-task 3 touches a different file (`records.py`) and depends on sub-task 1 being complete. Sub-tasks 4 and 5 are separate because they test different behaviors and may need to run in different Implementer or Test Engineer sessions.

---

## Exercise 2 — Match Pattern to Problem

**Type:** Pattern selection
**Time:** ~10 minutes

For each scenario, name the correct workflow pattern (Feature Delivery, Bug Investigation, or Refactor and Validate) and state one reason.

| # | Scenario |
|---|---------|
| 1 | A user reports that `send_alert()` sends duplicate notifications intermittently. The root cause is unknown. |
| 2 | A new endpoint `POST /api/notifications/preferences` needs to be added per a written API spec. |
| 3 | `notifications.py` has grown to 400 lines. The module works correctly but is hard to read. You want to split it into `notifications/dispatcher.py` and `notifications/preferences.py`. |
| 4 | `log_event()` silently drops events when `user_id` is None instead of raising a `ValueError`. The fix location is known. |
| 5 | The team wants to add audit logging to all write operations across `user.py`, `notifications.py`, and `auth.py`. There is no existing spec beyond "log all writes". |

**Expected answers:**

| # | Pattern | Reason |
|---|---------|--------|
| 1 | Bug Investigation | Root cause is unknown — start with Analyst to form a hypothesis before any implementation |
| 2 | Feature Delivery | A written spec exists; start with Planner to decompose into sub-tasks |
| 3 | Refactor and Validate | Behavior is correct; goal is structural improvement; no feature change |
| 4 | Bug Investigation | Root cause is known and the fix location is identified — Analyst step can be brief; Implementer can proceed immediately |
| 5 | Feature Delivery | New capability with cross-file scope; needs Planner decomposition and possibly Solution Architect for cross-module design |

---

## Exercise 3 — Spot the Decomposition Failure

**Type:** Diagnosis and rewrite
**Time:** ~15 minutes

The following sub-task list was produced by a Planner session. Review each sub-task and identify any violations of the 3-property rule (bounded scope, single acceptance criterion, no compound steps). Rewrite any broken sub-tasks.

**Sub-task list:**

```
1. Update the notification system to add preferences support and write tests.
2. Refactor notifications.py and update the README.
3. Add get_notification_preferences() to notifications.py.
4. Fix all edge cases in the data layer.
5. Implement update_notification_preferences() in notifications.py so that it validates
   input, persists changes, and handles missing user IDs.
```

**Expected answer:**

| Sub-task | Violation | Rewrite |
|----------|----------|---------|
| 1 | Compound steps ("and write tests") + two acceptance criteria | Split: (a) implement preferences support; (b) write tests for preferences |
| 2 | Compound steps ("and update the README") + two files | Split: (a) refactor `notifications.py`; (b) update `README.md` to reflect new structure |
| 3 | None — this is correctly formed | Keep as-is |
| 4 | No file named ("the data layer" is not a file); no acceptance criterion | Rewrite: "Fix `[specific function]` in `[named file]` so that `[specific behavior]`" |
| 5 | Three compound acceptance criteria (validate, persist, handle) | Split into three sub-tasks, one criterion each |

---

## Exercise 4 — Write a Workflow File

**Type:** Document authoring
**Time:** ~15 minutes

Using the feature request from Exercise 1 and your sub-task breakdown, produce a complete `workflow-feature-delivery.md` file. Use the anatomy from `theory.md`. Fill in all required sections including steps for all sub-tasks, the active context block, and leave the `## Outcome` section as a template to be filled in after execution.

**Expected answer:**

```markdown
<!-- Generated: 2026-04 -->

## Pattern
Feature Delivery

## Problem statement
Add user notification preferences to the existing notification system. Users must be able
to opt out of specific notification types (SYSTEM, ALERT, ACTIVITY). Success: all three
new/modified functions exist, all tests pass, and log_event() respects opt-outs. Out of
scope: UI for managing preferences, notification history, email delivery.

## Active context
- Instruction file: `.github/copilot-instructions.md`
- Architecture notes: none
- Constraints: type annotations required on all functions; pytest for tests; no plain-text
  storage for user data

## Steps
1. **Planner** → Input: this workflow file · Output: `feature-breakdown.md` ·
   Scope: read-only · Verify: 5 sub-tasks, each with one named file and one criterion
2. **Implementer** → Input: `feature-breakdown.md` sub-task 1 · Output: `notifications.py` ·
   Scope: `notifications.py` · Verify: `get_notification_preferences()` exists and returns correct type
3. **Implementer** → Input: sub-task 2 · Output: `notifications.py` ·
   Scope: `notifications.py` · Verify: `update_notification_preferences()` exists and persists
4. **Implementer** → Input: sub-task 3 · Output: `notifications.py` ·
   Scope: `notifications.py` · Verify: `log_event()` suppresses on opt-out
5. **Test Engineer** → Input: sub-tasks 4–5 · Output: `tests/test_notifications.py` ·
   Scope: `tests/test_notifications.py` · Verify: all tests pass
6. **Code Reviewer** → Input: full diff · Output: `review-findings.md` ·
   Scope: read-only · Verify: no blocking issues, or all blocking issues resolved

## Outcome
<!-- Fill in after completion -->
- Artifacts produced:
- Deviations from plan:
- Issues found:
```

---

## Exercise 5 — Write the Bug Investigation Handoff Chain

**Type:** Handoff authoring
**Time:** ~15 minutes

**Context:**

A bug has been reported: `log_event()` in `notifications.py` raises an unhandled `KeyError` when called with a user ID that has no registered preferences. The Analyst session has produced `root-cause.md` with the following findings:

> Root cause: `log_event()` accesses `_preferences[user_id]` without a default. If the user has no preferences record, a `KeyError` is raised. Fix location: line 47 of `notifications.py`, function `log_event()`. Recommended fix: use `_preferences.get(user_id, {})` and treat missing entry as "all enabled".

Write all three 3-part handoff prompts for this Bug Investigation workflow:
- Handoff A: Analyst → Implementer
- Handoff B: Implementer → Test Engineer
- Handoff C: Test Engineer → Code Reviewer

**Expected answer:**

**Handoff A — Analyst → Implementer:**

```
Summary: The Analyst session produced root-cause.md. Root cause: KeyError in log_event()
at notifications.py line 47 — dict access without default. Fix: use .get(user_id, {}).

Objective: Implementer — fix the KeyError in log_event() at notifications.py line 47.
Scope: notifications.py only. Do not modify any other file.

Carry-forward:
- Active instruction file: .github/copilot-instructions.md
- Type annotations required on all modified functions.
- Do not introduce new dependencies.
- Stop and signal completion when the fix is committed.
```

**Handoff B — Implementer → Test Engineer:**

```
Summary: The Implementer session fixed the KeyError in log_event() at notifications.py
line 47. Fix committed: _preferences.get(user_id, {}) replaces direct dict access.

Objective: Test Engineer — write a regression test confirming log_event() does not raise
KeyError when called with a user ID that has no preferences record.
Scope: tests/test_notifications.py only. Do not modify notifications.py.

Carry-forward:
- Active instruction file: .github/copilot-instructions.md
- Use pytest. Test must cover: (a) call with unknown user_id completes without exception;
  (b) event is treated as enabled for all types when no preferences record exists.
- Stop and signal completion when the test is committed and passing.
```

**Handoff C — Test Engineer → Code Reviewer:**

```
Summary: The Test Engineer added a regression test for the KeyError fix. Test committed
and passing in tests/test_notifications.py. The fix and the test cover the reported scenario.

Objective: Code Reviewer — review the fix in notifications.py (line 47 area) and the new
test in tests/test_notifications.py. Confirm no new issues were introduced.
Scope: read-only. Do not modify any file.

Carry-forward:
- Active instruction file: .github/copilot-instructions.md
- Check: fix does not change behavior for users with existing preferences.
- Check: test is specific, not fragile.
- Produce numbered findings. Mark each finding as BLOCKING or NON-BLOCKING.
```
