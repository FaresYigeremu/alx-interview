#!/usr/bin/python3
"""
0-island_permieter
"""
# File: 0-island_perimeter.py


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.
    :param grid: List of lists of integers where 0 water & 1  land.
    :return: Integer perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for the current land cell
                perimeter += 4
                # Check the top neighbor
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                # Check the left neighbor
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2
    return perimeter
