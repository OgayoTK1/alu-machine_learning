#!/usr/bin/env python3
"""
Write a function def cofactor(matrix): that calculates the cofactor
matrix of a matrix:

* matrix is a list of lists whose cofactor matrix should be calculated
* If matrix is not a list of lists, raise a TypeError with the
  message matrix must be a list of lists
* If matrix is not square or is empty, raise a ValueError with the
  message matrix must be a non-empty square matrix
* Returns: the cofactor matrix of matrix
"""


def cofactor(matrix):
    """Calculates the cofactor matrix of a given square matrix.

    Args:
        matrix: A list of lists representing the matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a non-empty square matrix.

    Returns:
        The cofactor matrix (list of lists).
    """
    if not isinstance(matrix, list) or not matrix or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    m = len(matrix[0])

    if any(len(row) != m for row in matrix) or n != m:
        raise ValueError("matrix must be a non-empty square matrix")

    def det(mat):
        """Recursive determinant using cofactor expansion along first row."""
        if not mat or not mat[0]:
            return 1

        cols = len(mat[0])
        res = 0
        for j in range(cols):
            sign = 1 if j % 2 == 0 else -1
            sub = [row[:j] + row[j + 1:] for row in mat[1:]]
            res += sign * mat[0][j] * det(sub)
        return res

    cofactors = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            submatrix = [
                matrix[r][:j] + matrix[r][j + 1:]
                for r in range(n) if r != i
            ]
            minor_det = det(submatrix)
            cofactor_val = ((-1) ** (i + j)) * minor_det
            cofactor_row.append(cofactor_val)
        cofactors.append(cofactor_row)

    return cofactors
