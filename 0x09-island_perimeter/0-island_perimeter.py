#!/usr/bin/python3
""" Permieter island
"""


def island_perimeter(grid):
    """ island perimeter function
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                continue
            if grid[i][j] == 1:
                try:
                    if i > 0 and grid[i - 1][j] == 0:
                        perimeter += 1
                    if i < len(grid) - 1 and grid[i + 1][j] == 0:
                        perimeter += 1
                    if j > 0 and grid[i][j - 1] == 0:
                        perimeter += 1
                    if j < len(grid[i]) - 1 and grid[i][j + 1] == 0:
                        perimeter += 1
                except IndexError:
                    pass
    return (perimeter)
