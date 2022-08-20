from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        not_found = True
        while l <= r:
            pivot = (r + l) // 2
            picked = nums[pivot] 
            if picked == target:
                return pivot 
            elif target > picked:
                l = pivot + 1 
            else:
                r = pivot - 1


if __name__ == "__main__":
    print("holla")
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9

    res = solution.search(nums, 9)

    assert(res, 4)