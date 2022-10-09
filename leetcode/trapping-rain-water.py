from typing import List


class Solution:
    def trap_O_N(self, height: List[int]) -> int:
        """
        Computation: O(n)
        Memory: O(n)
        """
        # Calculate an array with the max left height
        max_left_height = [0]
        max_height = 0
        for i in range(len(height)):
            max_height = max(max_height, height[i])
            max_left_height.append(max_height)

        # Calculate an array with the min right height
        max_right_height = [0]
        max_height = 0
        for i in range(len(height)-1, 0, -1):
            max_height = max(max_height, height[i])
            max_right_height.insert(0, max_height)

        # Calculate a list with the level of the water
        water_level = []

        for i in range(len(max_left_height) - 1):
            water = min(max_left_height[i], max_right_height[i]) - height[i]
            if water > 0:
                water_level.append(water)
            else:
                water_level.append(0)

        return sum(water_level)

    def trap(self, height: List[int]) -> int:
        """
        Computation: O(n)
        Memory: 1
        """
        maxL, maxR = height[0], height[-1]
        l, r = 0, len(height) - 1
        i = 0

        total_water_trapped = 0

        # Iterate until the left and right pointer crosses
        while (l < r):

            # Calculate the min between maxL and maxR to know which pointer has to switch
            if maxL <= maxR:
                l += 1
                i = l
            else:
                r -= 1
                i = r

            # Calculate the amount of water that can be hold in the current position
            water = min(maxL, maxR) - height[i]

            if water > 0:
                total_water_trapped += water

            # Update the maxL and maxR
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

            # Advance to the next position

            #print("maxL:" + str(maxL))
            #print("maxR:" + str(maxR))
            #print("i: " + str(i))
            #print("l: " + str(l))
            #print("r: " + str(l))

        return total_water_trapped


if __name__ == "__main__":
    solution = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    r = solution.trap(height)
    assert r == 6


    height = [5, 4, 1, 2]
    r = solution.trap(height)
    assert r == 1
