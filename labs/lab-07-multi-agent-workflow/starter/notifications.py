"""
notifications.py — Notification dispatch module.

Stub implementation for Lab 07. The Implementer session will add
get_notification_preferences() and update_notification_preferences(),
and modify log_event() to respect user preferences.
"""

from enum import Enum
from typing import Any


class NotificationType(Enum):
    """Supported notification types."""
    SYSTEM = "SYSTEM"
    ALERT = "ALERT"
    ACTIVITY = "ACTIVITY"


# In-memory preferences store.
# Key: user_id (str), Value: dict mapping NotificationType to enabled flag (bool).
# NOTE: accessing this dict without a default will raise KeyError for unknown users.
_preferences: dict[str, dict[NotificationType, bool]] = {}


# In-memory event queue for dispatched notifications.
_queue: list[dict[str, Any]] = []


def log_event(user_id: str, event_type: NotificationType, message: str) -> None:
    """
    Dispatch a notification event for the given user.

    TODO (sub-task 3): Check _preferences before dispatching.
    Currently dispatches unconditionally.
    """
    _queue.append({
        "user_id": user_id,
        "event_type": event_type,
        "message": message,
    })


def get_queue() -> list[dict[str, Any]]:
    """Return a copy of the current notification queue. Used in tests."""
    return list(_queue)


def clear_queue() -> None:
    """Clear the notification queue. Used in tests."""
    _queue.clear()


# TODO (sub-task 1): Implement get_notification_preferences(user_id: str) -> dict[NotificationType, bool]
# Returns the preference dict for the given user.
# If no preferences record exists, return all types as enabled.

# TODO (sub-task 2): Implement update_notification_preferences(user_id: str, prefs: dict[NotificationType, bool]) -> None
# Updates and persists the preference dict for the given user.
# Validate that all keys are NotificationType members.
