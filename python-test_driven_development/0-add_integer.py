#!/usr/bin/python3
"""
Module 0-add_integer
Provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the integer result.

    Floats are first casted to integers.
    Raises:
        TypeError: If a or b are not integers or floats, or if float is NaN or inf.

    Args:
        a (int or float): first number
        b (int or float): second number (default is 98)

    Returns:
        int: sum of a and b casted to integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # check for NaN or infinity
    if isinstance(a, float) and (a != a or a == float("inf") or a == float("-inf")):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b == float("inf") or b == float("-inf")):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
