#!/usr/bin/env python3
"""Module containing a function to calculate the shape of a matrix.
"""

def matrix_shape(matrix):
    """Calculates the shape of a matrix.

    Assumes the matrix is a (possibly nested) list with consistent dimensions
    in each level.

    Args:
        matrix: The matrix (nested list).

    Returns:
        list: The shape of the matrix as a list of integers.
    """
    shape = []
    current = matrix
    while isinstance(current, list):
        shape.append(len(current))
        if not current:
            break
        current = current[0]
    return shape
