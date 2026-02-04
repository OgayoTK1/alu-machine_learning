#!/usr/bin/env python3
"""
Write a function def determinant(matrix): that calculates the
determinant of a matrix:

* matrix is a list of lists whose determinant should be calculated
* If matrix is not a list of lists, raise a TypeError with the
  message matrix must be a list of lists
* If matrix is not square, raise a ValueError with the message
  matrix must be a square matrix
* The list [[]] represents a 0x0 matrix
* Returns: the determinant of matrix
"""

def determinant(matrix):
    """Calculates the determinant of a square matrix.
    
    Args:
        matrix: List of lists representing the matrix.
    
    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not a square matrix.
    
    Returns:
        The determinant of the matrix.
    """
    # Validate input: must be a list of lists (non-empty for access)
    if not isinstance(matrix, list) or not matrix or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    # For [[]], n=1, but inner list is empty
    m = len(matrix[0]) if matrix else 0

    # Check all rows have same length
    if any(len(row) != m for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Square check, with special allowance for 0x0 matrix [[]]
    if n != m and not (n == 1 and m == 0):
        raise ValueError("matrix must be a square matrix")

    # 0x0 matrix determinant is 1
    if n == 1 and m == 0:
        return 1

    # 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # Recursive cofactor expansion along first row
    det = 0
    for j in range(m):
        sign = 1 if j % 2 == 0 else -1
        # Submatrix excluding row 0 and column j
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += sign * matrix[0][j] * determinant(submatrix)

    return det
