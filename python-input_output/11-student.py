#!/usr/bin/python3
"""
Module 11-student
Contains a Student class with public attributes and
methods to_json(attrs=None) and reload_from_json(json) for
serialization and deserialization of the instance.
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
        Returns a dictionary representation of the Student instance.
        If attrs is a list of strings,
        only attributes in this list are included.
        Otherwise, all attributes are included.
        """
        all_attrs = self.__dict__
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: all_attrs[k] for k in attrs if k in all_attrs}
        return all_attrs.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with values from the provided dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
