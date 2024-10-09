#!/usr/bin/python3
"""
Pascal's triangle
"""
def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]  # The first row is always [1]

    for i in range(1, n):
        # Start the row with 1
        row = [1]
        # Each element in the middle is the sum of the two above it
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End the row with 1
        row.append(1)
        triangle.append(row)

    return triangle

