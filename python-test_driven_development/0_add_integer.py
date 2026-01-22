#!/usr/bin/python3
"""
This module defines a function add_integer that adds two integers.
It handles floats by casting them to integers and raises TypeError
if the arguments are not integers or floats.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (converted to integers).

    Args:
        a (int or float): first number
        b (int or float, optional): second number (default 98)

    Returns:
        int: the addition of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

