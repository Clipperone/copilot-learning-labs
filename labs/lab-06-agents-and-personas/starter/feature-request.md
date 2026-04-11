# Feature Request: User Event Notification System

## Context

The starter project is a minimal Flask API with user CRUD operations (`src/api/users.py`) backed by a `User` model (`src/models/user.py`). Currently there is no observability — no events are logged when users are created, updated, or deleted.

## Feature

Add an event notification system that logs a structured event whenever a user record changes state.

## Requirements

1. **Event types:** The system must support exactly three event types: `USER_CREATED`, `USER_UPDATED`, `USER_DELETED`.
2. **Log levels:**
   - `USER_CREATED` → `INFO`
   - `USER_UPDATED` → `DEBUG`
   - `USER_DELETED` → `INFO`
3. **Event payload:** Each log entry must include: event type, user ID, and a UTC timestamp.
4. **Integration points:** The event must be triggered from the route handler layer — not from the model layer. The model must not import from the notification module.
5. **No external dependencies:** Use the Python standard library `logging` module only. No third-party event bus or message queue.
6. **File location:** New notification code goes in `src/notifications.py` only. Do not create additional modules.

## Out of Scope

- Persistent event storage (database, file system)
- Asynchronous delivery
- Notification consumers or subscribers
- Email, webhook, or push delivery

## Acceptance Criteria

- `notifications.py` exports a `log_event(event_type, user_id)` function that accepts a string event type and an integer user ID.
- `log_event` raises `ValueError` if `event_type` is not one of the three valid types.
- Calling `log_event("USER_CREATED", 42)` emits an `INFO` log entry containing `USER_CREATED`, `42`, and a UTC timestamp.
- The route handlers in `users.py` call `log_event` at the appropriate points.
- All existing tests continue to pass after the integration.
