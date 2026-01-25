#!/usr/bin/python3
"""
Module 2-matrix_divided
Provides a function to divide all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix (list of lists of int/float): the matrix to divide
        div (int or float): the divisor

    Returns:
        list: new matrix with all elements divided by div, rounded to 2 decimals

    Raises:
        TypeError: if matrix is not a list of lists of int/float
        TypeError: if rows of the matrix are not all the same size
        TypeError: if div is not a number (int/float)
        ZeroDivisionError: if div is 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all((isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0 or any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]

