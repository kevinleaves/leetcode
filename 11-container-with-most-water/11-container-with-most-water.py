class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxWater = 0
        curWater = 0

        while l < r:
            lesserHeight = min([height[l], height[r]])
            curWater = lesserHeight * abs(r - l)
            maxWater = max(curWater, maxWater)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxWater