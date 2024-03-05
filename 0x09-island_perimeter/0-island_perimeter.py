#!/usr/bin/python3
""" Permieter island
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the given grid.
    Args:
      Returns:
      The perimeter of the island, or 0 if there is no island.
      """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row > 0 and grid[row - 1][col] == 0:
                    perimeter += 1
                if row < rows - 1 and grid[row + 1][col] == 0:
                    perimeter += 1
                if col > 0 and grid[row][col - 1] == 0:
                    perimeter += 1
                if col < cols - 1 and grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter
