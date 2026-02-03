"""Module that provides a function to concatenate two NumPy arrays along a given axis.
"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two numpy.ndarrays along a specific axis.

    Args:
        mat1: First ndarray.
        mat2: Second ndarray.
        axis: The axis along which to concatenate (default: 0).

    Returns:
        numpy.ndarray: A new array with mat1 and mat2 concatenated along the
        specified axis.
    """
    return np.concatenate((mat1, mat2), axis=axis)
