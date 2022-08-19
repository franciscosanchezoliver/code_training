from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        profit = 0
        
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            
            profit = max(profit, sell - buy)
            
            if buy > sell:
                l = r
                r += 1
            else:
                r += 1

        return profit



if __name__ == "__main__":
    print("hello")
    solution = Solution()

    prices = [7,1,5,3,6,4]
    res = solution.maxProfit(prices)
    assert(res, 5)
    
    prices = [7,6,4,3,1]
    res = solution.maxProfit(prices)
    assert(res, 0)
    

