from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Counter the number of characters in the string that we are searching
        s1_map = Counter(s1)

        windows_len = len(s1)

        for i in range(len(s2) - windows_len + 1):
            s2_windows = Counter(s2[i: i + windows_len])

            if s1_map == s2_windows:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()

    s1 = "ab"
    s2 = "eidbaooo"
    r = solution.checkInclusion(s1, s2)
    assert r == True

    s1 = "adc"
    s2 = "dcda"
    r = solution.checkInclusion(s1, s2)
    assert r == True
