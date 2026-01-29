#!/usr/bin/python3
"""Module 100-my_int: defines a rebel MyInt class"""


class MyInt(int):
    """MyInt class inherits from int and inverts == and !="""

    def __eq__(self, other):
        """Invert equality: return True if not equal"""
        return int(self) != other

    def __ne__(self, other):
        """Invert inequality: return True if equal"""
        return int(self) == other
