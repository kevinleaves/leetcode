class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      '''
      i: int[]
      o: int[]
      c: in place, O(1) space requires only constant memory to store prefix sum
      
      init variable to store running sum
      iterate from 0 to n - 1 idx
        add element at i to sum
        replace element at i with sum
      '''

      prefixSum = 0
      for i in range(len(nums)):
        prefixSum += nums[i]
        nums[i] = prefixSum
      return nums

      
      