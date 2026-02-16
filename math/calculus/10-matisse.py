#!/usr/bin/env python3
"""
10. Derive happiness in oneself from a good day's work

Mandatory task implementing the derivative of a polynomial represented as
a list of coefficients.

The input list poly represents the polynomial where:
- poly[0] is the constant term (x^0)
- poly[1] is the coefficient of x^1
- ...
- poly[n] is the coefficient of x^n

The function returns a new list representing the coefficients of the derivative,
trimming trailing zeros (minimal representation).
- If the derivative is the zero polynomial, returns [0]
- If the input is invalid (not a non-empty list of numbers), returns None
"""

def poly_derivative(poly):
    """
    Compute the derivative of the polynomial represented by poly.

    Args:
        poly (list): List of numeric coefficients (int or float).

    Returns:
        list: Coefficients of the derivative polynomial (trimmed).
        [0]: If the derivative is the zero polynomial.
        None: If poly is invalid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    for coeff in poly:
        if not isinstance(coeff, (int, float)):
            return None

    # Build derivative coefficients: i * poly[i] for i >= 1
    der = []
    for i in range(1, len(poly)):
        der.append(poly[i] * i)

    # If constant polynomial, derivative is zero
    if not der:
        return [0]

    # Trim trailing zeros
    while der and der[-1] == 0:
        der.pop()

    # If all coefficients were zero after trimming
    if not der:
        return [0]

    return der
