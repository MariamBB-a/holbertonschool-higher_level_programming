#!/usr/bin/python3
"""Module that adds two integers"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int or float): first number
        b (int or float): second number

    Raises:
        TypeError: if a or b is not an integer or float
        TypeError: if a or b is NaN or infinite

    Returns:
        int: addition of a and b
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
