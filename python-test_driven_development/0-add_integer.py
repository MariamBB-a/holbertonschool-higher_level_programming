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

    try:
        a = int(a)
    except Exception:
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except Exception:
        raise TypeError("b must be an integer")

    return a + b
