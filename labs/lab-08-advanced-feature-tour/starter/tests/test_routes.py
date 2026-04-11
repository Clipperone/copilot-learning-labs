"""Tests for api/routes.py — starter file for Lab 08.

Coverage is intentionally incomplete; Task 4 asks you to run these tests
and verify they pass using the corrected command from Task 3.

Run from labs/lab-08-advanced-feature-tour/ using:
    PYTHONPATH=starter pytest starter/tests/
On Windows PowerShell:
    $env:PYTHONPATH="starter"; pytest starter/tests/
"""
from api.routes import get_item, list_items


def test_get_item_returns_existing_item():
    item = get_item("1", "user-a")
    assert item == {"id": "1", "name": "Widget", "owner_id": "user-a"}


def test_get_item_returns_none_for_missing_id():
    assert get_item("999", "user-a") is None


def test_list_items_returns_all_items():
    items = list_items("user-a")
    assert len(items) == 2


# TODO Lab 08 Extension: after implementing delete_item(), add tests for:
#   - delete_item() removes the item when called by the owner
#   - delete_item() raises ValueError for a non-existent item_id
#   - delete_item() raises PermissionError when called by a non-owner
