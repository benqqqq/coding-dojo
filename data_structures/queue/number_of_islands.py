


"""
find all islands
    0
 0  1  0
    0

this is an island

  0 0
0 1 1 0
  0 0

island is not connected to island

"""
from queue import Queue
from typing import List

"""
island_count = 0
for each row:
    for each column:
        if cell is visited:
            break

        if cell is water:
            break

        island_count += 1
        bfs this element()


bfs_island(i, j)
    queue = []

    queue.push((i, j))

    while !queue.is_empty():
        cell = queue.dequeue()
        visit this cell
        if cell.right:
            queue.push(cell.right)
        if cell.bottom:
            queue.push(cell.bottom)

    if cell is visited:
        return
"""

class Map:
    def __init__(self, grid) -> None:
        self.grid = grid
        self.visited_pos = set()
        self.width = len(grid[0])
        self.height = len(grid)
        self.island = '1'  # water = '0'

    def visit(self, i, j):
        self.visited_pos.add((i, j))

    def is_visited(self, i, j):
        return (i, j) in self.visited_pos

    def is_outside(self, i, j):
        return not (
            0 <= i < self.height and
            0 <= j < self.width
        )

    def is_island(self, i, j):
        return self.grid[i][j] == self.island


class Solution:

    def __init__(self) -> None:
        self.map = None

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.map = Map(grid)

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                count += self.bfs_visit_island(i, j)

        return count

    def bfs_visit_island(self, i, j):
        queue = Queue()
        queue.put((i, j))
        visited_island = False

        while not queue.empty():
            x, y = queue.get()

            if (
                self.map.is_visited(x, y) or
                self.map.is_outside(x, y) or
                not self.map.is_island(x, y)
            ):
                continue

            self.map.visit(x, y)
            visited_island = True

            queue.put((x + 1, y))  # right
            queue.put((x, y + 1))  # down
            queue.put((x - 1, y))  # left
            queue.put((x, y - 1))  # up

        return 1 if visited_island else 0


if __name__ == '__main__':
    s = Solution()
    assert s.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1

    assert s.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3

    assert s.numIslands([["1"]]) == 1
