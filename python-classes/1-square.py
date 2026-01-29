#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: size of the square (no validation for now)
        """
        self.__size = size
