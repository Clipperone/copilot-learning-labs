"""
user.py — User model stub.

Read-only reference for Lab 07. The Implementer session must not
modify this file during sub-task 1 or sub-task 2 of the notification
preferences feature. It is included to represent realistic cross-file
scope temptation.
"""

from dataclasses import dataclass


@dataclass
class User:
    """Minimal user record."""
    user_id: str
    display_name: str
    email: str


# In-memory user store. Populated at startup in a real application.
_users: dict[str, User] = {
    "u001": User(user_id="u001", display_name="Alice", email="alice@example.com"),
    "u002": User(user_id="u002", display_name="Bob", email="bob@example.com"),
}


def get_user(user_id: str) -> User | None:
    """Return the User for the given user_id, or None if not found."""
    return _users.get(user_id)


def user_exists(user_id: str) -> bool:
    """Return True if a user record exists for the given user_id."""
    return user_id in _users
