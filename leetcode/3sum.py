
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Here will be store the result of the exercise 
        res = []

        # First we have to order the list => O(n * log n)
        nums.sort()

        # We need 3 pointers to resolve the equation:
        #   a + b + c = 0
        # 
        # b and c is the same as the left and right pointers in the problem 2Sum
        target = 0
        a = 0 
        r = len(nums) - 1

        while a < len(nums) - 2:
            l = a + 1 
            r = len(nums) - 1

            while l < r :
                if nums[a] + nums[l] + nums[r] > target: 
                    r -= 1
                elif nums[a] + nums[l] + nums[r] < target:
                    l += 1
                    while l < r and nums[l] == nums[l-1] and nums[l] < nums[r]:
                        l += 1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            

            a += 1
            while nums[a] == nums[a - 1] and a < len(nums) - 2:
                a += 1

        return res


if __name__ == "__main__":
    solution = Solution()

    #nums = [-3, 3, 4, -3, -1, 2]
    #output  = [[-1,-1,2],[-1,0,1]]
    #res = solution.threeSum(nums)
    #assert  res == output

    nums = [-1,0,1,2,-1,-4]
    output  = [[-1,-1,2],[-1,0,1]]
    res = solution.threeSum(nums)
    assert  res == output

    nums = [0,0,0,0]
    output  = [[0,0,0]]
    res = solution.threeSum(nums)
    assert  res == output

    nums = [-1,0,1,0]
    res = solution.threeSum(nums)
    assert res == [[-1,0,1]]
    

    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    res = solution.threeSum(nums)
    assert res == [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]


    nums = [-4,-1,-4,0,2,-2,-4,-3,2,-3,2,3,3,-4]
    res = solution.threeSum(nums)
    assert res == [[-4,2,2],[-3,0,3],[-2,-1,3],[-2,0,2]] 