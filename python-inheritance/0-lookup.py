#!/usr/bin/python3
"""Defines a function that returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        list: A list containing the names of attributes and methods.
    """
    return dir(obj)
