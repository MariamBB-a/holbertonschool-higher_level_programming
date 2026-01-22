#!/usr/bin/python3
"""
0-add_integer module
This module contains a function that adds two integers or floats
after casting floats to integers. Raises TypeError if arguments
are not integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result as an integer.
    
    Floats are first casted to integers.
    Raises TypeError if a or b is not an integer or float.
    
    Args:
        a (int or float): first number
        b (int or float, optional): second number, defaults to 98

    Returns:
        int: sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

