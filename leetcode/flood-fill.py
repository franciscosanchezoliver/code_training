from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr_color = image[sr][sc]
        h = len(image)
        w = len(image[0])

        def dfs(sr, sc):
            if 0 <= sr < h and 0 <= sc < w and image[sr][sc] == curr_color and image[sr][sc] != color:
                image[sr][sc] = color
                dfs(sr + 1, sc)
                dfs(sr - 1, sc)
                dfs(sr, sc + 1)
                dfs(sr, sc - 1)

        dfs(sr, sc)
        return image


if __name__ == "__main__":
    solution = Solution()

    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2

    res = solution.floodFill(image, sr, sc, color)

    assert ([[2, 2, 2], [2, 2, 0], [2, 0, 1]], res)
