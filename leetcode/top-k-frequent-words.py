from typing import List
from functools import cmp_to_key
from collections import Counter


class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def compare(pair1, pair2):
            str1 = pair1[0]
            count1 = pair1[1]

            str2 = pair2[0]
            count2 = pair2[1]

            if count1 < count2:
                return 1
            elif count1 > count2:
                return -1
            else:
                if str1 < str2:
                    return -1
                if str1 > str2:
                    return 1
                else:
                    return 0

        words = Counter(words)
        most_common_words = words.most_common()
        most_common_words = sorted(most_common_words, key=cmp_to_key(compare))
        res = [word[0] for word in most_common_words][:k]
        return res


if __name__ == "__main__":
    solution = Solution()
    #words = ["i","love","leetcode","i","love","coding"]
    #k = 2
    #res = solution.topKFrequent(words, k)
    #assert res == ["i","love"]

    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    res = solution.topKFrequent(words, k)
    assert res == ["i", "love", "coding"]
