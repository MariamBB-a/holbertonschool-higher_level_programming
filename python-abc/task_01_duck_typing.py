#!/usr/bin/python3
"""Circle and Rectangle classes with duck
typing for area and perimeter"""


import math


class Shape:
    """Base Shape class (optional abstract interface)"""

    def area(self):
        raise NotImplementedError("area() is not implemented")

    def perimeter(self):
        raise NotImplementedError("perimeter() is not implemented")


class Circle(Shape):
    """Circle shape"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of any shape using duck typing"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
