class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        i: int[], val: int
        o: int[] w/ vals removed and all non-val integers moved to the left side. same len as num
        c: in place so O(1) space
        e: 
        '''
        # instantiate left and right pointers
        # left at 0
        # right at last idx of array
        l, r = 0, len(nums) - 1
        count = 0
        # while left <= right
        while l <= r:
          # while right is equal to val
          while r >= 0 and nums[r] == val:
            # decrement right
            r -= 1
            count += 1

          # if nums[left] is val
          if l <= r and nums[l] == val:
            # swap nums at left and right
            nums[l], nums[r] = nums[r], nums[l]
            # decrement right
            r -= 1
            count += 1
        
          # increment left
          l += 1
        return len(nums) - count
        
        