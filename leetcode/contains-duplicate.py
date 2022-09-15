class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        char_set = set()
        for each_num in nums:
            if each_num not in char_set:
                char_set.add(each_num)
            else:
                return True
        return False


