#!/usr/bin/env python3
"""
Write a function def definiteness(matrix): that calculates the
definiteness of a matrix:

* matrix is a numpy.ndarray of shape (n, n) whose definiteness should
  be calculated
* If matrix is not a numpy.ndarray, raise a TypeError with the
  message matrix must be a numpy.ndarray
* If matrix is not a valid matrix, return None
* Return: the string Positive definite, Positive semi-definite,
  Negative semi-definite, Negative definite, or Indefinite if the
  matrix is positive definite, positive semi-definite, negative
  semi-definite, negative definite or indefinite, respectively
* If matrix does not fit any of the above categories, return None
* You may import numpy as np
"""

import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a square matrix.

    Args:
        matrix: numpy.ndarray of shape (n, n).

    Raises:
        TypeError: If matrix is not a numpy.ndarray.

    Returns:
        str: "Positive definite", "Positive semi-definite",
             "Negative definite", "Negative semi-definite",
             "Indefinite", or None.
    """
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if (matrix.ndim != 2 or
        matrix.shape[0] != matrix.shape[1] or
        matrix.shape[0] == 0):
        return None

    eigvals = np.linalg.eigvals(matrix)

    # If significant imaginary part, not real symmetric -> invalid
    if np.any(np.abs(np.imag(eigvals)) > 1e-10):
        return None

    real_eigs = np.real(eigvals)
    min_eig = np.min(real_eigs)
    max_eig = np.max(real_eigs)

    tol = 1e-10

    if min_eig > tol:
        return "Positive definite"
    if max_eig < -tol:
        return "Negative definite"
    if min_eig > -tol:
        return "Positive semi-definite"
    if max_eig < tol:
        return "Negative semi-definite"
    return "Indefinite"
