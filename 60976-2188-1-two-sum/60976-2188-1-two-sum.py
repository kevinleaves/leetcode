class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      '''
      there will always be a solution
      i: int[], unsorted
      o: return indices of the numbers that add up to the target
      c: no constraints, or less than n^2
      e: 
      '''

      for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
          if nums[i] + nums[j] == target:
            return [i, j]

            
        