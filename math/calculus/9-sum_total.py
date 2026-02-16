#!/usr/bin/env python3
"""
9. Our life is the sum total of all the decisions we make every day,
and those decisions are determined by our priorities

Mandatory task implementing the summation of squares using the closed-form
formula (no loops allowed):

∑_{i=1}^n i² = n(n + 1)(2n + 1) / 6

The function returns the integer sum for positive integer n,
or None if n is invalid (not a positive integer).
"""

def summation_i_squared(n):
    """
    Compute the sum of squares from 1 to n using the closed-form formula.

    Args:
        n (int): Upper limit of the summation (must be a positive integer).

    Returns:
        int: The sum 1² + 2² + ... + n².
        None: If n is not a positive integer.
    """
    if not isinstance(n, int) or n < 1:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
