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

    # Reject NaN
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    # Reject infinity
    if a in (float("inf"), float("-inf")):
        raise TypeError("a must be an integer")
    if b in (float("inf"), float("-inf")):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

