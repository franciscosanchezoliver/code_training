from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h = len(grid)
        w = len(grid[0])
        visited = [[0 for x in range(w)] for y in range(h)]
        islands = 0

        def bfs(x, y):
            q = deque()
            directions = [
                [1, 0],
                [0, 1],
                [-1, 0],
                [0, -1],
            ]
            q.append((x, y))
            while q:
                curr = q.pop()
                visited[curr[0]][curr[1]] = 1
                for dir_y, dir_x in directions:
                    new_y = curr[0] + dir_y
                    new_x = curr[1] + dir_x

                    if 0 <= new_y < h \
                            and 0 <= new_x < w \
                            and visited[new_y][new_x] == 0 \
                            and grid[new_y][new_x] != '0':
                        q.append((new_y, new_x))

        for x in range(h):
            for y in range(w):
                val = grid[x][y]
                visit = visited[x][y]

                if val == "1" and visit == 0:
                    bfs(x, y)
                    islands += 1

        return islands


if __name__ == "__main__":
    solution = Solution()

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    res = solution.numIslands(grid)
    assert (res, 1)

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    res = solution.numIslands(grid)
    assert (res, 3)
