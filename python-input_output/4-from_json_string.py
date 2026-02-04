#!/usr/bin/python3
"""
Module 4-from_json_string
Contains a function that returns a Python object
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """Returns a Python data structure represented by a JSON string."""
    return json.loads(my_str)
