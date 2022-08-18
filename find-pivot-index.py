from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        center = 0
        sum_left = 0
        sum_right = 0

        for i in range(len(nums)):
            center = nums[i]
            if i > 0:
                sum_left += nums[i - 1]
            
            sum_right = total - sum_left - center
            if sum_left == sum_right:
                return i
        return -1


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 7, 3, 6, 5, 6]
    result = solution.pivotIndex(nums)
    assert (result == 3)
