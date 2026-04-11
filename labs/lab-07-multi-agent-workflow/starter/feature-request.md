# Feature Request: Notification Preferences

**Requester:** Product team
**Date:** 2026-04
**Priority:** Medium

---

## Summary

Users need the ability to opt out of specific notification types. Currently, all users receive all notifications regardless of preference. There is no way to suppress a notification type per user.

---

## Background

The notification system dispatches three types of events:

- `SYSTEM` — automated alerts from the platform (e.g., maintenance windows, account changes)
- `ALERT` — threshold-based warnings triggered by monitoring rules
- `ACTIVITY` — user-initiated actions and activity feed updates

All three types are sent to every user unconditionally. Support tickets show that `ACTIVITY` notifications are the most frequently reported as unwanted.

---

## Requirements

1. Users must be able to retrieve their current notification preferences as a dict mapping each notification type to an enabled/disabled flag.
2. Users must be able to update their notification preferences, enabling or disabling individual types.
3. The `log_event()` function must respect user preferences before dispatching a notification — if a user has disabled a notification type, `log_event()` must not dispatch for that type and that user.
4. All new and modified functions must have type annotations.
5. Data must not be stored in plain text.

---

## Out of Scope

- UI for managing preferences (separate ticket)
- Email notification delivery (separate system)
- Notification history or audit log
- Bulk updates across multiple users in a single call

---

## Affected Files

| File | Relationship |
|------|-------------|
| `labs/lab-07-multi-agent-workflow/starter/notifications.py` | Primary implementation target |
| `labs/lab-07-multi-agent-workflow/starter/user.py` | User model — read only for this feature; do not modify |

---

## Acceptance

The feature is complete when:

- `get_notification_preferences(user_id)` exists in `notifications.py` and returns `dict[NotificationType, bool]`
- `update_notification_preferences(user_id, prefs)` exists in `notifications.py` and persists changes
- `log_event()` suppresses dispatch when the user has disabled the relevant notification type
- All functions have type annotations
- At least one test per new function exists and passes
