#!/usr/bin/python3
"""
Defines Shape-like classes using duck typing.
"""


class Circle:
    """Circle class."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        pi = 3.141592653589793
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        pi = 3.141592653589793
        return 2 * pi * self.radius


class Rectangle:
    """Rectangle class."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter using duck typing.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
