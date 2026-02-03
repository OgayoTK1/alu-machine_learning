#!/usr/bin/env python3
"""Module that provides a function for matrix multiplication
of two 2D matrices.
"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication on two 2D matrices.

    Args:
        mat1: First 2D matrix (list of lists of ints/floats).
        mat2: Second 2D matrix (list of lists of ints/floats).

    Returns:
        A new 2D matrix with the multiplication result if mat1
        and mat2 are compatible (columns of mat1 == rows of mat2),
        otherwise None.
    """
    if (not mat1 or not mat2 or len(mat1[0]) != len(mat2)):
        return None

    return [
        [
            sum(mat1[i][k] * mat2[k][j] for k in range(len(mat1[0])))
            for j in range(len(mat2[0]))
        ]
        for i in range(len(mat1))
    ]
