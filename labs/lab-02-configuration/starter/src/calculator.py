"""
Calculator module — starter file for Lab 02.

This file is intentionally minimal. It contains no type annotations,
no docstrings, and uses inconsistent spacing to give you realistic
lint signals when Ruff is configured.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
