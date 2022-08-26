
from tkinter import W


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if ( (c1 in mapST and mapST[c1] != c2) or
            (c2 in mapTS and mapTS[c2] != c1)):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1
            
        return True


if __name__ =="__main__":
    solution = Solution()

    s = "egg"
    t = "add"
    assert(solution.isIsomorphic(s, t), True)

    s = "foo"
    t = "bar"
    assert(solution.isIsomorphic(s, t), False)

    s = "badc"
    t = "baba"
    result = solution.isIsomorphic(s, t)
    assert(result, False)

