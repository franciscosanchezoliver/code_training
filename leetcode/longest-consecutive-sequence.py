from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_series_length = 0 

        for i in range(len(nums)):
            number_picked = nums[i]
            j = 1 

            # Search if the number has a left child.
            if (number_picked - 1) not in set_nums:

                # If the number doesnt have a number-1 then its 
                # the left of the series. Then we need to start counting from the start of the series 
                # and see how far we go
                while (nums[i] + j) in set_nums:
                    j += 1

                max_series_length = max(max_series_length, j)
            
        return max_series_length


if __name__ =="__main__":
    solution = Solution()

    nums = [100,4,200,1,3,2]
    res = solution.longestConsecutive(nums)
    assert res == 4


    nums = [0,3,7,2,5,8,4,6,0,1]
    res = solution.longestConsecutive(nums)
    assert res == 9