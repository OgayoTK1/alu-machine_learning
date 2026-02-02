#!/usr/bin/env python3
def matrix_shape(matrix):
    shape = []
    current = matrix
    while isinstance(current, list) and current:
        shape.append(len(current))
        current = current[0]
    return shape
