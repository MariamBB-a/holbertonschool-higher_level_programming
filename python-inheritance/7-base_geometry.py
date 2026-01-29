#!/usr/bin/python3
"""Module 7-base_geometry: defines BaseGeometry class"""


class BaseGeometry:
    """Base class for geometric operations"""

    def area(self):
        """Raises an exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): name of the variable
            value (int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
