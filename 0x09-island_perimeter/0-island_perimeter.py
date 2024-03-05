#!/usr/bin/python3
""" Permieter island
"""


def island_perimeter(grid):
    """ island perimeter function
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                try:
                    if grid[i - 1][j] == 0:
                        perimeter += 1
                    if grid[i + 1][j] == 0:
                        perimeter += 1
                    if grid[i][j - 1] == 0:
                        perimeter += 1
                    if grid[i][j + 1] == 0:
                        perimeter += 1
                except IndexError:
                    pass
    return (perimeter)
