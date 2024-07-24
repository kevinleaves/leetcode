class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      # static array to return
      res = [0]*len(nums)

      # first item of res and the prefix sum are initialized as the first number of nums
      res[0], prefixSum = nums[0], nums[0]

      # iterate from index 1 onwards, updating the prefix sum and res as we go
      for i in range(1, len(nums)):
        prefixSum += nums[i]
        res[i] = prefixSum

      return res