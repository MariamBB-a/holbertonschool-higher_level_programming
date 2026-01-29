#!/usr/bin/python3
"""Function that returns True if the object is
an instance of a class that inherited (directly
or indirectly) from the specified class."""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class
    that inherits from a_class
    (directly or indirectly).

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj inherits from a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

