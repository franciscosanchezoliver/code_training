class Solution:
    def characterReplacement_old(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = {}

        for r in range(len(s)):
            # Keep score of how many times a character appears
            count[s[r]] = 1 + count.get(s[r], 0)

            # Condition to move left point to right
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(r-l+1, res)
        return res


if __name__ == "__main__":
    solution = Solution()
    #s = "ABAB"
    #k = 2
    #res = solution.characterReplacement(s, k)
    #assert res == 2

    s = "AABABBA"
    k = 1
    res = solution.characterReplacement(s, k)
    assert res == 4
