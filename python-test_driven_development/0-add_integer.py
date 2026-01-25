#!/usr/bin/python3
"""
Module: 0-add_integer
Provides a function that adds two integers or floats.
Floats are cast to integers before addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a (int or float): first number
        b (int or float, optional): second number (default is 98)

    Returns:
        int: sum of a and b, after converting floats to integers

    Raises:
        TypeError: if a or b is not an integer or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
