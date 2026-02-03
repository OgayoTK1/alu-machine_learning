#!/usr/bin/env python3
"""Module that provides a function to concatenate two 2D
matrices along a given axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a specific axis.

    Args:
        mat1: First 2D matrix (list of lists of ints/floats).
        mat2: Second 2D matrix (list of lists of ints/floats).
        axis: 0 for vertical, 1 for horizontal concatenation.

    Returns:
        New 2D matrix if shapes are compatible along the axis,
        otherwise None. Rows are copied to avoid shared references.
    """
    if axis == 0:
        if mat1 and mat2 and len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1 + mat2]

    if len(mat1) != len(mat2):
        return None
    return [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]
