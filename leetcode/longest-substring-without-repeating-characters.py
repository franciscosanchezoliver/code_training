
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        res = 0 
        char_set = set()
        
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            res = max(res, r - l + 1)

        return res


if __name__ == "__main__":
    solution = Solution()
    #s = "abcabcbb"
    #assert(solution.lengthOfLongestSubstring(s) == 3)

    s = "pwwkew"
    result = solution.lengthOfLongestSubstring(s) 
    assert(result== 3)
