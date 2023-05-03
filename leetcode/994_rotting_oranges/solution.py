from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))

        def rotten(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                return
            grid[x][y] = 2
            queue.append((x, y))

        # start from -1 to skip the first round rotten
        elapsed_minutes = -1

        while len(queue) > 0:
            for k in range(len(queue)):
                i, j = queue.popleft()
                rotten(i + 1, j)
                rotten(i, j + 1)
                rotten(i - 1, j)
                rotten(i, j - 1)

            elapsed_minutes += 1

        # for the case there is no rotten orange, elapsed minutes should be 0
        elapsed_minutes = max(elapsed_minutes, 0)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # there is still some fresh orange
                    return -1

        return elapsed_minutes
