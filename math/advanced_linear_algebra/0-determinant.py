#!/usr/bin/env python3
def determinant(matrix):
    """
    Calculates the determinant of a square matrix represented as a list of lists.
    
    Args:
        matrix: A list of lists representing the matrix.
    
    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is not square.
    
    Returns:
        The determinant of the matrix.
    """
    # Type validation: must be a non-empty list of lists
    if (not isinstance(matrix, list) or
        not matrix or
        not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    # Get dimensions
    rows = len(matrix)
    cols = len(matrix[0])

    # Validate all rows have the same length
    if any(len(row) != cols for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Validate square matrix (special case for 0x0 matrix represented as [[]])
    if rows != cols and not (rows == 1 and cols == 0):
        raise ValueError("matrix must be a square matrix")

    # Special case: 0x0 matrix [[]] has determinant 1
    if rows == 1 and cols == 0:
        return 1

    # Base case: 1x1 matrix
    if rows == 1:
        return matrix[0][0]

    # General case: cofactor expansion along the first row
    det = 0
    for j in range(cols):
        # Sign for cofactor (alternates + - + - ...)
        sign = 1 if j % 2 == 0 else -1
        
        # Build submatrix by removing first row and column j
        sub_matrix = [
            matrix[i][:j] + matrix[i][j+1:]
            for i in range(1, rows)
        ]
        
        # Recursive call
        det += sign * matrix[0][j] * determinant(sub_matrix)
    
    return det
