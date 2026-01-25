#!/usr/bin/python3
"""This module contains a function that adds two integers.
It converts floats to integers and raises TypeError for invalid types.
"""


def add_integer(a, b=98):
    """Add two integers safely.

    Args:
        a (int or float): first number
        b (int or float, optional): second number, defaults to 98

    Raises:
        TypeError: if a or b is not an integer or float, or cannot be converted

    Returns:
        int: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        a = int(a)
    except (ValueError, OverflowError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (ValueError, OverflowError):
        raise TypeError("b must be an integer")

    return a + b
