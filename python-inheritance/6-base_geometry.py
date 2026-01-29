#!/usr/bin/python3
"""
Module that defines class BaseGeometry.
"""


class BaseGeometry:
    """BaseGeometry class with an unimplemented area method."""

    def area(self):
        """Raises an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
