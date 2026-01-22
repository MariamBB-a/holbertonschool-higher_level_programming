#!/usr/bin/python3
"""
Module 0-add_integer
Contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b.
    Floats are cast to integers.
    Raises TypeError if a or b are not integers or floats.

    Args:
        a (int/float): first number
        b (int/float, optional): second number, default 98

    Returns:
        int: sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

