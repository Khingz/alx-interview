#!/usr/bin/python3
""" Permieter island
"""


def island_perimeter(grid):
    perimeter = 0
    if not grid:  # Empty grid
        return perimeter

    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 to perimeter
                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # If top neighbor is land, subtract 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # If left neighbor is land, subtract 2

    return perimeter
