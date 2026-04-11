"""API route handlers — starter file for Lab 08.

Used in Task 1 (Plan mode) and Task 2 (AI-assisted code review).
"""
from typing import Any

# In-memory store — replaces a real database for this lab.
_items: dict[str, dict[str, Any]] = {
    "1": {"id": "1", "name": "Widget", "owner_id": "user-a"},
    "2": {"id": "2", "name": "Gadget", "owner_id": "user-b"},
}


def get_item(item_id: str, requesting_user_id: str) -> dict[str, Any] | None:
    """Return item by ID if it exists, or None if not found."""
    return _items.get(item_id)


def list_items(requesting_user_id: str) -> list[dict[str, Any]]:
    """Return all items regardless of owner."""
    return list(_items.values())


# TODO Lab 08 Task 1: use Plan mode to design delete_item() before writing any code.
#
# Feature specification:
#   - Function signature: delete_item(item_id: str, requesting_user_id: str) -> None
#   - Only the owner of an item may delete it.
#   - Deleting a non-existent item raises ValueError.
#   - Deleting an item the requesting user does not own raises PermissionError.
#   - All deletions must be audited before the item is removed.
#
# Complete Task 1 (Plan mode design) before writing any implementation here.
