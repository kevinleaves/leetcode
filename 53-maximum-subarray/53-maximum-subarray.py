class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for n in nums:
            print(f"n = {n}")
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSum = max(currSum, maxSum)
            print(f"currSum = {currSum}")
        return maxSum