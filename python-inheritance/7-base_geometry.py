#!/usr/bin/python3
"""
Module 7-base_geometry
Defines class BaseGeometry with area() and integer_validator()
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer > 0

        Args:
            name (str): name of the parameter
            value (int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
