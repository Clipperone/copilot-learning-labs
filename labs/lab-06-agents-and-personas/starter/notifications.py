# notifications.py
# Stub file — used as scope reference for Implementer and Test Engineer sessions.
# Do not modify this file before running the Planner session in Task 2.
# The Planner session will produce a task breakdown for implementing this module.
# An Implementer session will fill in each function following the task breakdown.

import logging
from typing import Final

# TODO: Implementer — define VALID_EVENT_TYPES as a frozenset of the three event type strings.
VALID_EVENT_TYPES: Final[frozenset] = frozenset()

# TODO: Implementer — configure a module-level logger named "notifications".
logger = logging.getLogger(__name__)


def log_event(event_type: str, user_id: int) -> None:
    """Log a structured user event.

    Args:
        event_type: One of USER_CREATED, USER_UPDATED, USER_DELETED.
        user_id: The integer ID of the affected user.

    Raises:
        ValueError: If event_type is not a valid event type.
    """
    # TODO: Implementer — implement this function per the feature request requirements.
    raise NotImplementedError
