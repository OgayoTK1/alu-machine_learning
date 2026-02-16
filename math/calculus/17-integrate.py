#!/usr/bin/env python3
"""
Module for calculating the indefinite integral of a polynomial.
"""

def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.

    Args:
        poly (list): List of numeric coefficients representing the polynomial,
                     where index i corresponds to the coefficient of x^i.
        C (int or float, optional): Integration constant. Defaults to 0.

    Returns:
        list: New list of coefficients representing the integral polynomial,
              with trailing zeros removed and whole-number coefficients as integers.
              Returns None if poly is not a valid list of numbers or C is invalid.
    """
    if not isinstance(poly, list) or not isinstance(C, (int, float)):
        return None

    if poly and not all(isinstance(coef, (int, float)) for coef in poly):
        return None

    # Start with the integration constant
    integral = [float(C)]

    # Compute integral coefficients: coef_i / (i + 1) for new power i+1
    for i in range(len(poly)):
        new_coef = poly[i] / (i + 1)
        integral.append(new_coef)

    # Convert to int if the float is a whole number
    integral = [
        int(coef) if isinstance(coef, float) and coef.is_integer() else coef
        for coef in integral
    ]

    # Remove trailing zeros to make the list as small as possible
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
