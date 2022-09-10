import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # If the input list is empty return 0
        if len(stones) == 0: 
            return 0 

        # If there is just one rock then return the weight of that rock
        if len(stones) == 1:
            return stones[0]

        # Library heapq doesn't have Max heap so invert the values of the array 
        # te create a max heap
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]

        # Create a heap with the list of rocks
        heapq.heapify(stones)

        # Get the 2 biggest stones
        while(len(stones) > 1):

            rock1 = heapq.heappop(stones)
            rock2 = heapq.heappop(stones)

            rock_after_smash = abs(rock1 - rock2)

            # The result rock is the subtraction of the 2 rocks
            # The result rock comes back into the heap
            if rock_after_smash > 0: 
                heapq.heappush(stones, -1 * rock_after_smash)
        
            # if there is only one stone left
            # then return the value of this stone as result of the problem
            if len(stones) == 1:
                return -1 * stones[0]
            if len(stones) == 0:
                return 0


if __name__ == "__main__":
    solution = Solution()
    #stones = [2,7,4,1,8,1]
    #res = solution.lastStoneWeight(stones)
    #assert res == 1

    stones = [1,3]
    res = solution.lastStoneWeight(stones)
    assert res == 2