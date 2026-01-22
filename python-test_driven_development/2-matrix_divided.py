#!/usr/bin/python3
"""
Module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): matrix of integers or floats
        div (int or float): divisor

    Returns:
        list of lists: new matrix with divided values
    """

    # Validate matrix
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(row for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)

    return new_matrix

