#!/usr/bin/python3
"""
Module 8-class_to_json
Contains a function that returns the dictionary description
withdata structures (list, dictionary, string, integer, boolean)
for JSON serialization of a class instance.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a class instance
    suitable for JSON serialization.
    """
    return obj.__dict__.copy()
