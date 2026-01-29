#!/usr/bin/python3
"""Module 101-add_attribute:
adds a new attribute to an object if possible"""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible.

    Raises:
        TypeError: if the object can't have a new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
