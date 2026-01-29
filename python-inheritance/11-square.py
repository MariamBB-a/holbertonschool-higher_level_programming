#!/usr/bin/python3
"""Module 11-square: defines a Square 
class inheriting from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a square with size

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Compute the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description"""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
