#!/usr/bin/python3
""" Rotate a 2D matrix by 90deg clockwose
"""


def rotate_2d_matrix(matrix):
    """Matrix method
    """
    row_len = len(matrix[0])

    for i in range(row_len - 1, -1, -1):
        for j in range(row_len):
            matrix[j].append(matrix[i].pop(0))
