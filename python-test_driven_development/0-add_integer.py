#!/usr/bin/python3
"""This module contains a function that adds two integers.
It converts floats to integers and raises TypeError for invalid types,
including NaN or infinite floats.
"""


def add_integer(a, b=98):
    """Add two integers safely.

    Args:
        a (int or float): first number
        b (int or float, optional): second number, defaults to 98

    Raises:
        TypeError: if a or b is not an integer/float, or cannot be converted
                   (NaN or infinite float)
                   
    Returns:
        int: the addition of a and b
    """
    # Check types
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN or infinity
    for value, name in ((a, "a"), (b, "b")):
        if isinstance(value, float):
            if value != value or value in (float("inf"), float("-inf")):
                raise TypeError(f"{name} must be an integer")

    # Convert floats to integers
    return int(a) + int(b)
