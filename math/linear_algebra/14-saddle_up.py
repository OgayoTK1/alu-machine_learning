#!/usr/bin/env python3
"""Module that provides a function for matrix multiplication
using NumPy.
"""


import numpy as np


def np_matmul(mat1, mat2):
    """Performs matrix multiplication on two numpy.ndarrays.

    Args:
        mat1: First ndarray (2D or higher).
        mat2: Second ndarray (2D or higher).

    Returns:
        numpy.ndarray: A new array containing the matrix
        product of mat1 and mat2.
    """
    return np.matmul(mat1, mat2)
