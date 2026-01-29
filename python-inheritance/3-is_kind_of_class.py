#!/usr/bin/python3
"""
Module that defines a function 'is_kind_of_class' which
checks if an object is an instance of a specified class or
an instance of a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or of a class
    that inherited from a_class, else False.

    Args:
        obj (any type): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance or subclass instance of a_class, else False.
    """
    return isinstance(obj, a_class)
