
class Solution:
    def climbStairs(self, n: int) -> int:

        prev1 = 0
        prev2 = 1 
        sum = 0
        for i in range(n):
            sum = prev1 + prev2 
            prev1 = prev2
            prev2 = sum
        
        return sum


if __name__ == "__main__":
    solution = Solution()
    res = solution.climbStairs(5)
    print(res)
    assert(res, 8)

    res = solution.climbStairs(1)
    print(res)
    assert(res, 8)