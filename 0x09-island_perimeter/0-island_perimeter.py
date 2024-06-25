#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
     Returns the perimeter of the island described in grid.

     Args:
     - grid (list of lists of integers): Represents the island grid.
       0 represents a water zone, and 1 represents a land zone.
       The grid is completely surrounded by water.

     Returns:
     - int: Perimeter of the island.
     """
    visit = set()

    def dfs(i, j):
        """
         DFS helper function for calculating the perimeter.

         Args:
         - i : Row index of the current position.
         - j : Column index of the current position.

         Returns:
         - int: Contribution to the perimeter for the current position.
         """
        if i >= len(grid) or j >= len(grid[0]) or\
                i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visit:
            return 0
        visit.add((i, j))
        perimeter = 0
        perimeter += dfs(i, j + 1)
        perimeter += dfs(i + 1, j)
        perimeter += dfs(i, j - 1)
        perimeter += dfs(i - 1, j)
        return perimeter
    total_perimeter = 0
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value:
                total_perimeter += dfs(i, j)
    return total_perimeter
