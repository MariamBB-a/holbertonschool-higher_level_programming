#!/usr/bin/python3
"""Function to check if an object is an instance
of a class or inherits from it"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or is
    an instance of a class that inherited from,
    the specified class; otherwise False.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance or inherits from a_class, else False.
    """
    return isinstance(obj, a_class)
