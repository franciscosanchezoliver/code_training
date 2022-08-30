from msvcrt import open_osfhandle
from typing import List
from collections import Counter


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:

        # Array with the index of the anagrams
        res = []

        # We have to count how many chars are in p
        char_counter_p = {}
        for each_char in p:
            if each_char not in char_counter_p:
                char_counter_p[each_char] = 1
            else:
                char_counter_p[each_char] += 1

        char_counter_subs = {}

        # Iterate over the longest string to count how many char of each type there are
        # We use a sliding windows to avoid to count each iteration
        i, l = 0, 0 
        while i < len(s):
            # The current char
            next_char = s[i]

            # Add current char and delete left char
            if next_char not in char_counter_subs:
                char_counter_subs[next_char] = 1
            else:
                char_counter_subs[next_char] += 1

            if i - l + 1 > len(p):
                # The char that left the sliding windows
                left_char_of_windows = s[l]
                char_counter_subs[left_char_of_windows] -= 1  # Delete left char
                # Delete from dictionary if there are 0 char
                if char_counter_subs[left_char_of_windows] == 0:
                    char_counter_subs.pop(left_char_of_windows)
                l += 1

            if char_counter_p == char_counter_subs:
                res.append(l)

            i += 1

        return res

    def findAnagrams_fails_because_time_exceed(self, s: str, p: str) -> List[int]:
        res = []

        def checkIfTheyAreAnagram(subs, p):
            counterSubs = Counter(subs)
            counterP = Counter(p)
            return counterSubs == counterP

        for i in range(len(s)):
            # Get a substring as big as p in each position
            subs = s[i: i + len(p)]

            areAnagram = checkIfTheyAreAnagram(subs, p)
            if areAnagram:
                res.append(i)

        return res


if __name__ == "__main__":
    solution = Solution()

    s = "cbaebabacd"
    p = "abc"
    res = solution.findAnagrams(s, p)
    assert res == [0, 6]

    s = "abab"
    p = "ab"
    solution.findAnagrams(s, p)
