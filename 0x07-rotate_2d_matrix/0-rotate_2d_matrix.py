#!/usr/bin/python3
"""0-rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a matrix 90 degrees clockwise."""
    # Make transpose of the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # reverse the matrix
    for i in range(len(matrix)):
        matrix[i].reverse()
