#!/usr/bin/env python3
"""Module that provides a function for element-wise addition of two arrays.
"""


def add_arrays(arr1, arr2):
    """Adds two arrays element-wise.

    Args:
        arr1: List of ints/floats.
        arr2: List of ints/floats.

    Returns:
        A new list containing the element-wise sums if arr1 and arr2 have the
        same shape (length), otherwise None.
    """
    if len(arr1) != len(arr2):
        return None

    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result
