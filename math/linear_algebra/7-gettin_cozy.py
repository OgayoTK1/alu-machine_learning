"""Module that provides a function for concatenating two 2D matrices along a given axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a specific axis.

    Args:
        mat1: First 2D matrix (list of lists of ints/floats).
        mat2: Second 2D matrix (list of lists of ints/floats).
        axis: The axis along which to concatenate (0 for vertical, 1 for horizontal).

    Returns:
        A new 2D matrix with the concatenated result if the matrices are compatible
        along the given axis, otherwise None.

    The function creates new row lists (using slicing) to ensure the returned matrix
        is independent of the input matrices (in-place modifications to inputs do not
        affect the result).
    """
    if axis == 0:
        # Vertical concatenation: must have same number of columns
        if mat1 and mat2 and len(mat1[0]) != len(mat2[0]):
            return None
        # Concatenate rows and copy each row to avoid shared references
        return [row[:] for row in mat1 + mat2]

    # axis == 1: Horizontal concatenation: must have same number of rows
    if len(mat1) != len(mat2):
        return None

    # Build new rows by concatenating corresponding rows from mat1 and mat2
    return [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]
