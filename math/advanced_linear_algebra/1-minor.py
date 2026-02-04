#!/usr/bin/env python3
"""
Write a function def minor(matrix): that calculates the minor
matrix of a matrix:

* matrix is a list of lists whose minor matrix should be calculated
* If matrix is not a list of lists, raise a TypeError with the
  message matrix must be a list of lists
* If matrix is not square or is empty, raise a ValueError with the
  message matrix must be a non-empty square matrix
* Returns: the minor matrix of matrix
"""


def minor(matrix):
    """Calculates the minor matrix of a given square matrix.

    Args:
        matrix: A list of lists representing the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.

    Returns:
        The minor matrix (list of lists).
    """
    if not isinstance(matrix, list) or not matrix or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    m = len(matrix[0])

    if any(len(row) != m for row in matrix) or n != m or n == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    def det(mat):
        """Recursive determinant using cofactor expansion along first row."""
        if not mat:
            return 1

        cols = len(mat[0])
        res = 0
        for j in range(cols):
            sign = 1 if j % 2 == 0 else -1
            sub = [row[:j] + row[j + 1:] for row in mat[1:]]
            res += sign * mat[0][j] * det(sub)
        return res

    minors = []
    for i in range(n):
        minor_row = []
        for j in range(n):
            sub = [[matrix[k][l] for l in range(n) if l != j]
                   for k in range(n) if k != i]
            minor_row.append(det(sub))
        minors.append(minor_row)

    return minors
