#!/usr/bin/python3
"""Defines a function to generate Pascal's triangle."""


def pascal_triangle(n):
    """
    Return a list of lists of integers
      Pascal's triangle of n rows.

    - Returns an empty list if n <= 0.
    - n is assumed to be an integer.
    """
    if n <= 0:
        return []
    # Initialize triangle with the first row
    triangle = [[1]]
    # Generate subsequent rows
    for i in range(1, n):
        prev_row = triangle[-1]
        # Start each row with 1
        row = [1]
        # Compute intermediate values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        # End each row with 1
        row.append(1)
        triangle.append(row)
    return triangle
