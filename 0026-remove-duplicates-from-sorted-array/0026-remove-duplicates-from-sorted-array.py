class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      """
      I: sorted int[] size n
      O: int[] of size n w/ duplicates removed. unique elements of k, k <= n
      C: in-place solution O(1) space
      E:
      """
      
      l = 1

      for r in range(1, len(nums)):
        # if curr number 
        if nums[r] != nums[r - 1]:
          nums[l] = nums[r]
          l += 1
      
      return l 