class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
      '''
      res
      increment res when we find a pair of indices where the nums at the indices sum to LESS than the target

      brute force test all pairs via two pointers

      '''
      # if there are no pairs, return 0
      if len(nums) < 2:
        return 0
      
      res = 0
      for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
          pairSum = nums[i] + nums[j]
          if pairSum < target:
            res += 1

      return res
        