#!/usr/bin/env python3
"""Module that provides a function for element-wise operations
on two NumPy arrays.
"""


def np_elementwise(mat1, mat2):
    """Performs element-wise addition, subtraction, multiplication,
    and division.

    Args:
        mat1: A numpy.ndarray.
        mat2: A value interpretable as a numpy.ndarray
            (array or scalar).

    Returns:
        tuple: Containing the element-wise sum, difference, product,
               and quotient (in that order), leveraging NumPy
               broadcasting and true division.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
