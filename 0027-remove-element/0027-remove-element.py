class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
          return 0

        l = 0
        r = 0

        while r < len(nums):
          # conditional
          if nums[r] != val:
            # overwrite L with R
            nums[l] = nums[r]
            l += 1
          
          r += 1
          
        return l