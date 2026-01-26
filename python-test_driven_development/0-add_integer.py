#!/usr/bin/python3
"""
Module that adds two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    a and b must be integers or floats
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle NaN without imports
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
