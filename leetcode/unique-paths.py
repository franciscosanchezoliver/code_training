
from importlib.resources import path
from tkinter import W


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        """
        With dynamic programming
        """
        # Initialize a matrix with the last row all 1 and the last column all 1
        # Ex:
        # 0 0 0 1
        # 0 0 0 1
        # 1 1 1 1
        matrix = [[0] * (n - 1) + [1] for j in range(m - 1)] + [[1] * n]

        # Iterate over the matrix calculating the paths
        for x in range(n - 2, -1, -1):
            for y in range(m - 2, -1, -1):
                # Calculate the value for this cells based on its right and bottom
                matrix[y][x] = matrix[y + 1][x] + matrix[y][x + 1]

        return matrix[0][0]

    def uniquePaths_recursive(self, m: int, n: int) -> int:
        def dfs(x, y):
            if x >= n or y >= m:
                return 0
            elif x == n-1 and y == m-1:
                print("path found:" + str((str(y), str(x))))
                return 1
            else:
                print("visited" + str((str(y), str(x))))

            res = dfs(x + 1, y) + dfs(x, y + 1)
            return res

        res = dfs(0, 0)
        return res


if __name__ == "__main__":
    solution = Solution()
    m = 2
    n = 3
    print(solution.uniquePaths(m, n))
