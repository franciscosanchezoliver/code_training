import numbers
from re import A
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 3, 4]
        # output = [24, 12, 8, 6]

        nums_of_zeros = 0
        pre, pos, res = [0]*len(nums), [0]*len(nums), [0]*len(nums)

        pre_total, pos_total = 1, 1

        # Fill the pre and post arrays with the cum multiplication
        i = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] != 0:
                pre_total *= nums[i]
            else:
                nums_of_zeros += 1
                # If there are more than 2 zeros in the input array then all
                # elements of the result will be 0, so there is no more 
                # calculations needed
                if nums_of_zeros > 1:
                    return [0] * len(nums)
            pre[i] = pre_total

            if nums[j] != 0:
                pos_total *= nums[j]
            pos[j] = pos_total

            i += 1
            j -= 1


        # Calculate the result array
        pre_value, pos_value = 1, 1
        for i in range(len(nums)):
            if i - 1 < 0:
                pre_value = 1
            else:
                pre_value = pre[i - 1]

            if i + 1 > len(nums) - 1:
                pos_value = 1
            else:
                pos_value = pos[i + 1]

            # If there is 1 zero in the array and this position is not the zero
            # then its 0 the result, only in the 0 position we will have to 
            # calculate
            if nums_of_zeros == 0:
                res[i] = pre_value * pos_value
            elif nums_of_zeros == 1:
                # Check if this is the 0 position
                if nums[i] == 0 :
                    res[i] = pre_value * pos_value
                else:
                    res[i] = 0


        return res

    def productExceptSelfWithDivision(self, nums: List[int]) -> List[int]:

        # Protection for empty array as input
        if nums == []:
            return []

        # Variable to store the total sum of the multiplication
        # We can initialize the variable with the first element of the array
        total_multiplication = 1

        # If there is one 0 in the array the multiplication of the rest elements
        # its going o be 0.
        # If there are more than 1 zeros, then all elements would be 0
        numbers_of_ceros = 0
        # First we have to multiply every element of the array
        # for num in enumerate(nums:
        for i in range(0, len(nums)):
            # if the number is a 0 we have to pass this
            if nums[i] != 0:
                total_multiplication *= nums[i]
            else:
                numbers_of_ceros += 1

        # Calculate each element of the result array dividing the total
        # but that number
        res = []

        for num in nums:
            if numbers_of_ceros == 0:
                # To return an in use //
                res.append(total_multiplication // num)

            # Especial case when there are 0 in the array
            elif numbers_of_ceros == 1:
                if num == 0:
                    # If there is 0 in the array then the only places we have to calculate is
                    # in the 0 positions.
                    # Ant he result is the total multiplication
                    res.append(total_multiplication)  # To return an in use //
                else:
                    # If there is 0 in the array and the num is not 0 then the result
                    # we know its 0, because any number multiply by 0 is 0
                    res.append(0)
            # If there are at least 2 0 then all elements in the result are going to be 0
            elif numbers_of_ceros > 1:
                return [0] * len(nums)

        return res


if __name__ == "__main__":
    print("hello")
    solution = Solution()

    # Case without 0 in the array
    nums = [1, 2, 3, 4]
    output = [24, 12, 8, 6]
    result = solution.productExceptSelf(nums)
    assert result == output

    # Case with 0 in the array
    nums = [-1, 1, 0, -3, 3]
    output = [0, 0, 9, 0, 0]
    result = solution.productExceptSelf(nums)
    assert result == output

    nums = [2, 3, 0, 0]
    output = [0, 0, 0, 0]
    result = solution.productExceptSelf(nums)
    assert result == output

    nums = [2, 2, 0, 2, 2, 0, 0, 2, 2]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = solution.productExceptSelf(nums)
    assert result == expected

    nums = [0, 2, 3, 4]
    expected = [6, 0, 0, 0]
    result = solution.productExceptSelf(nums)
    assert result == expected
