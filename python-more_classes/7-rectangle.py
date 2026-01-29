#!/usr/bin/python3
"""Defines a Rectangle class with width, height, area, perimeter, and print_symbol."""


class Rectangle:
    """Class that defines a rectangle and tracks instances."""

    number_of_instances = 0  # class attribute to count instances
    print_symbol = "#"       # symbol used for string representation

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        If width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string with the rectangle represented by print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        sym = str(self.print_symbol)
        return "\n".join(sym * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Return a string representation that can recreate the object."""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance is deleted and decrement instance counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
