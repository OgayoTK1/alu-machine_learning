"""Module that provides a function to transpose a NumPy array.
"""


def np_transpose(matrix):
    """Transposes a numpy.ndarray by reversing its axes.

    Args:
        matrix: A numpy.ndarray of any dimension.

    Returns:
        numpy.ndarray: A new ndarray representing the transpose (matrix.T).
    """
    return matrix.T
