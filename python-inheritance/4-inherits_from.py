#!/usr/bin/python3
"""
Module that defines a function 'inherits_from'
which checks ifan object is an instance of a
class that inherited (directly
or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class
    that inherited from a_class (but not if obj is
    exactly an instance of a_class).

    Args:
        obj (any type): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj inherits from a_class, else False.
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
