from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        l, r = 0, len(height) - 1

        while l < r:
            
            print( l , r)

            height_l = height[l]
            height_r = height[r]

            # Calculate the min of both heights
            min_height = min(height_l, height_r)

            # Calculate the width 
            width = abs(l - r)

            # Calculate the area 
            area = width * min_height 

            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area





if __name__ == "__main__":
    print("hello")
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    res = solution.maxArea(height)
    assert (res , 49)

