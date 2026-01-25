#!/usr/bin/python3
"""Function that adds two integers
"""


def add_integer(a, b=98):
    """Adds two integers or floats, casting floats to integers."""

    # Type checks
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Prevent float overflow or NaN
    if isinstance(a, float) and (a != a or a == float('inf') or a == float('-inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b == float('inf') or b == float('-inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
