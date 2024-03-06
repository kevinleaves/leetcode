class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [-10000, -10001, -10002, 1, 2, 3]
        # calculate a running prefix sum
        # if prefix sum is ever negative, chop off the left side of the array
        # update res with running total
        # return res
        res = nums[0]
        left = 0
        runningSum = 0
        for right in range(len(nums)):
          if runningSum < 0:
            left += 1
            runningSum = 0
            
          runningSum += nums[right]
          
          # once we have a valid left pointer
          res = max(res, runningSum)
        return res
        

          