# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right, = 1, n
        badVersion =  n # last version is sure bad
        
        while left <= right:
            center = (right + left)//2
            isBad = isBadVersion(center)
            if isBad:
                right = center - 1
                badVersion = min(badVersion, center)
            else:
                left = center + 1
        return badVersion


if __name__ == "__main__":
    solution = Solution()
    res = solution.firstBadVersion(5)