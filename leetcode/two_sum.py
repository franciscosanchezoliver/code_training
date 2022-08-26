from typing import List

class Solution:

    def twoSum(
        self, 
        nums: List[int], 
        target:int
    ) -> List[int]:

        # Search if there is already a number that sums up the target amount
        target_found_in_list = list(filter(lambda number : number == target, nums)).__len__()
        if target_found_in_list > 0:
            return [nums.index(target)]

        # Filter numbers greater than the target. This will reduce the space of searching
        nums = [number for number in nums if number <= target]

        for first_number_index, first_number in enumerate (nums):
            for second_number_index, second_number in enumerate(nums):
                if first_number + second_number == target and \
                   first_number_index != second_number_index:
                    return [first_number_index, second_number_index]


if __name__ == '__main__':
    solution = Solution()
    resultado = solution.twoSum(nums = [2, 7, 11, 15], 
                                target= 9)
