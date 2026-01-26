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
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = None
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Let Python raise ZeroDivisionError naturally
    if div == 0:
        1 / div

    new_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)

    return new_matrix
