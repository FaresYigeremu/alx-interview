#!/usr/bin/python3
"""
0. Pascal's Triangle
"""
def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        row = [1]  # First element is always 1
        # Calculate middle elements
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
