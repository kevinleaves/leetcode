class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # SELECTION SORT (ON^2)
        writeIdx = 0
        while writeIdx < len(nums):
          # find index of the smallest number          
          lowestValIdx = writeIdx
          for i in range(writeIdx, len(nums)):
            if nums[i] < nums[lowestValIdx]:
              lowestValIdx = i
          nums[writeIdx], nums[lowestValIdx] = nums[lowestValIdx], nums[writeIdx]
          writeIdx += 1
        
        