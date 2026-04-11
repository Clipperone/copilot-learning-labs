<!-- Generated: 2026-04 -->
<!-- Reference solution for Lab 07 Task 1. Complete this independently before reading. -->

## Pattern

Feature Delivery

---

## Problem statement

Add user notification preferences to the existing notification system. Users must be able
to retrieve their current notification preferences (a mapping of notification type to
enabled/disabled flag) and update them. The `log_event()` function must respect opt-outs
and suppress dispatch when a user has disabled a notification type.

Success: `get_notification_preferences()`, `update_notification_preferences()`, and a
modified `log_event()` all exist in `notifications.py`, all new functions have type
annotations, and tests pass for each new function.

Out of scope: UI for managing preferences, email delivery, notification history, bulk
updates, and any changes to `user.py`.

---

## Active context

- Instruction file: `.github/copilot-instructions.md`
- Architecture notes: none — this feature is self-contained within `notifications.py`
- Constraints (from instruction file):
  - Type annotations required on all new and modified functions
  - Use pytest for tests
  - No plain-text storage for user data
  - Do not use MD5 or equivalent for any data handling

---

## Steps

1. **Planner** →
   Input: `labs/lab-07-multi-agent-workflow/starter/feature-request.md` (read-only) ·
   Output: `labs/lab-07-multi-agent-workflow/starter/feature-breakdown.md` ·
   Scope: read-only ·
   Verify: 4–6 sub-tasks, each with a named file and one acceptance criterion, no compound steps

2. **Implementer** →
   Input: `feature-breakdown.md` sub-task 1 ·
   Output: `labs/lab-07-multi-agent-workflow/starter/notifications.py` ·
   Scope: `notifications.py` only — do not open or modify `user.py` or any test file ·
   Verify: `get_notification_preferences(user_id)` exists and returns `dict[NotificationType, bool]`

3. **Implementer** →
   Input: `feature-breakdown.md` sub-task 2 ·
   Output: `labs/lab-07-multi-agent-workflow/starter/notifications.py` ·
   Scope: `notifications.py` only ·
   Verify: `update_notification_preferences(user_id, prefs)` exists and persists changes to `_preferences`

4. **Implementer** →
   Input: `feature-breakdown.md` sub-task 3 ·
   Output: `labs/lab-07-multi-agent-workflow/starter/notifications.py` ·
   Scope: `notifications.py` only ·
   Verify: `log_event()` does not dispatch when the user's preference for that type is `False`

5. **Code Reviewer** →
   Input: full diff of `notifications.py` across steps 2–4 ·
   Output: `labs/lab-07-multi-agent-workflow/starter/review-findings.md` ·
   Scope: read-only — `notifications.py` only ·
   Verify: findings are numbered, each marked BLOCKING or NON-BLOCKING; no source file was modified

---

## Outcome

<!-- Fill in after completing all lab tasks -->
- Artifacts produced:
- Deviations from plan:
- Issues found:
