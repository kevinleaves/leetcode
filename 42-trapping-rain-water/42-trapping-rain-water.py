class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
        # we want leftMax and Rightmax to be Equal
            if leftMax < rightMax:
                l += 1
                # calc new leftMax
                leftMax = max(leftMax, height[l])
                # this is the key: amt of water trapped at position => min(maxL, maxR) - current height
                # we don't have to do this min(maxL, maxR) calc because of our control flow. we just take maxL
                # leftMax - height[l] cannot be negative if we perform actions in this order
                res += leftMax - height[l]
            else: # if leftmax >= rightMax => do the same on the right side
                r -= 1
                # calc new rightMax
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res