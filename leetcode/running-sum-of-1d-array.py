from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i] 
            res.append(sum)

        return res


if __name__ =="__main__":
    print("hola")
    solution = Solution()

    nums = [1,2,3,4]
    resultado = solution.runningSum(nums)
    print(resultado)

    assert(resultado == [1,3,6,10])