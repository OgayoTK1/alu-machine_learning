#!/usr/bin/env python3
"""Module that provides a function for element-wise addition of two 2D matrices.
"""


def add_matrices2D(mat1, mat2):
    """Adds two 2D matrices element-wise.

    Args:
        mat1: 2D list of ints/floats.
        mat2: 2D list of ints/floats.

    Returns:
        A new 2D list containing the element-wise sums if mat1 and mat2 have the
        same shape, otherwise None.
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    return [
        [mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
        for i in range(len(mat1))
    ]
