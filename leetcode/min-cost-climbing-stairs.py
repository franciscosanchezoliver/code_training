from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


if __name__ == "__main__":
    solution = Solution()

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    res = solution.minCostClimbingStairs(cost)
    assert res == 6

    cost = [10, 15, 20]
    res = solution.minCostClimbingStairs(cost)
    assert res == 15
