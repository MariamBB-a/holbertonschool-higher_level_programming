#!/usr/bin/python3
"""
Module 9-student
Contains a Student class with public attributes and
a method to_json() returns a dictionary representation
of the instance.
"""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the  instance,
        suitable for JSON serialization.
        """
        return self.__dict__.copy()
