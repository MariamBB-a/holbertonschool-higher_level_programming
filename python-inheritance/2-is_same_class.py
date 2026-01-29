#!/usr/bin/python3
"""
Module that defines a function 'is_same_class' which
checks if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, else False.

    Args:
        obj (any type): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, else False.
    """
    return type(obj) is a_class
