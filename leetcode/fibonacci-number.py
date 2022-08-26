class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0: return 0
        if n == 1: return 1
        
        prev1, prev2 = 0, 1
        res = 0 
        
        for i in range(2, n + 1):
            res = prev1 + prev2
            prev1 = prev2
            prev2 = res
        
        return res

    def fib_recursive(self, n:int) -> int:
        if n == 0: return 0 
        if n == 1: return 1

        return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)
            
if __name__ == "__main__":
    solution = Solution()
    n = 4
    res = solution.fib(n)
    assert(res, 4)


    res = solution.fib_recursive(n)
    assert(res, 4)