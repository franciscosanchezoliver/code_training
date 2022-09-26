from tkinter import W
from typing import List


class Solution:
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order. 
    Find two numbers such that they add up to a specific target number. Let these two 
    numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
    Return the indices of the two numbers, index1 and index2, added by one as an integer 
    array [index1, index2] of length 2. The tests are generated such that there is exactly 
    one solution. You may not use the same element twice.
    Your solution must use only constant extra space.
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        O(n): The pointer never cross each other
        """
        l, r = 0, len(numbers) - 1

        while l < r:

            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]
    

    def twoSum_brute_force(self, numbers: List[int], target: int) -> List[int]:
        """
        O(n^2)
        """
        l, r  = 0, 1

        # They assure that the result can be found
        while True:

            # If the sum is greater than the target, then we dont have to
            # continue iterating. We can increment left and start again
            if ( r >= len(numbers)) or (numbers[l] + numbers[r] > target):
                l += 1
                r = l + 1

            # If the sum is less than the target we can increment the right pointer
            elif numbers[l] + numbers[r] < target:
                r += 1

            # the result is found. The indices in this problem start with 0 so we 
            # have to add one to both indices
            else:
                return [l + 1, r + 1]



if __name__ == "__main__":
    solution = Solution()

    nums = [1, 3, 4, 5, 7, 10, 11]
    target = 9
    res = solution.twoSum(numbers=nums, target=target)
    assert res == [3, 4]

    nums = [5, 25, 75]
    target = 100
    res = solution.twoSum(numbers=nums, target=target)
    assert res == [2, 3]
