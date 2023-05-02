from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        width = len(grid[0])
        height = len(grid)

        def visit(x: int, y: int) -> None:
            visited.add((x, y))

            # visit neighbors
            neighbors = [
                (x - 1, y) if x > 0 else None,
                (x, y - 1) if y > 0 else None,
                (x + 1, y) if x < (height - 1) else None,
                (x, y + 1) if y < (width - 1) else None,
            ]
            neighbors = [n for n in neighbors if n]

            for m, n in neighbors:
                if grid[m][n] == '1' and (m, n) not in visited:
                    visit(m, n)

        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    if (i, j) not in visited:
                        num_islands += 1
                        visit(i, j)

        return num_islands
