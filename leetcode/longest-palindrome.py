class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        char_map = {}
        center = 0
        for i in range(len(s)):
            if s[i] not in char_map:
                char_map[s[i]] = 1
            else:
                char_map[s[i]] += 1

        for each_char in char_map:
            if char_map[each_char] % 2 == 0:
                res += char_map[each_char]
            elif char_map[each_char] == 1:
                center = 1
        
        return res + center


if __name__ == "__main__":
    solution = Solution()

    #s = "abccccdd"
    #res = solution.longestPalindrome(s)
    #assert(res, 7)

    s = "ccc"
    res = solution.longestPalindrome(s)
    assert(res, 0)
