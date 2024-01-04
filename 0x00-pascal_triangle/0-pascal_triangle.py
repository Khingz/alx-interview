#!/usr/bin/python3
"""
 returns a list of lists of integers rep the Pascal’s triangle
"""


def pascal_triangle(n):
    """Return pascal triangle"""
    if n <= 0:
        return []
    arr = []
    for i in range(n):
        new_arr = []
        for j in range(i + 1):
            if j == 0 or j == i:
                new_arr.append(1)
            else:
                prev = arr[i-1][j-1] if j - 1 < len(arr[i-1]) else 0
                next_el = arr[i-1][j] if j < len(arr[i-1]) else 0
                new_el = prev + next_el
                new_arr.append(new_el)
        arr.append(new_arr)
    return arr
