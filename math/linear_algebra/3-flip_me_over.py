#!/usr/bin/env python3
"""Module for transposing a 2D matrix.
"""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix.

    Args:
        matrix: A 2D list (matrix) of ints/floats.

    Returns:
        list: A new 2D list representing the transpose of the input matrix.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

