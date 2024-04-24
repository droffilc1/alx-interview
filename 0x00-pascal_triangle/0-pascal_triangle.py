#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """Returns Pascal's triangle up to the given number of rows

    Args:
        n (int): The number of rows in the triangle

    Returns:
        list: Pascal's triangle represented as a list of lists
    """
    # Check if the list is empty
    if n <= 0:
        return []

    # Initialize the Pascal's triangle
    triangle = []

    # Generate each row
    for i in range(n):
        row = [1]  # First element is always 1
        if i > 0:
            # Generate the elements in between
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # Last element is always 1
        triangle.append(row)
    return triangle
