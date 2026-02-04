#!/usr/bin/python3
"""
Module 10-student
Contains a Student class with public attributes and
a method to_json(attrs=None) that returns a dictionary
representation of the instance. If attrs is a list of strings,
only those attributes are included.
"""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the  instance.
        If attrs is a list of strings, only attributes
        in this list are included.
        Otherwise, all attributes are included.
        """
        all_attrs = self.__dict__
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            # Filter only the requested attributes that exist
            return {k: all_attrs[k] for k in attrs if k in all_attrs}
        return all_attrs.copy()
