#!/usr/bin/python3
"""Function that adds two integers.
"""


def add_integer(a, b=98):
    """Adds two integers or floats, casting floats to integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
        # Reject NaN and Infinity
    for val, name in [(a, "a"), (b, "b")]:
        if isinstance(val, float):
            if val != val or val == float('inf') or val == float('-inf'):
                raise TypeError(f"{name} must be an integer")

    # Cast to int and return sum
    return int(a) + int(b)
