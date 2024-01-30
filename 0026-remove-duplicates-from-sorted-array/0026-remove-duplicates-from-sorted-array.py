class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        i: array of sorted ints (could be negative)
        o: same array of nums => duplicates moved to the end of the array, modified in place. 
        return k number of unique elements in nums
        c: O(1) space,
        e: initial nums length? array of length 1 -> return 1
        '''

        if len(nums) == 1:
          return 1

#         if len(nums) == 2:
#           if nums[0] != nums[1]:
#             return 2
#           else:
#             return 1
        
        # initialize k unique elements 
        k = 1

        # assume that first element is always slotted correctly. start first pointer at 2nd element
        # and start iterating from the 3rd element
        left = 1
        for right in range(1, len(nums)):
          if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
            k += 1
        # if left element and right element equal, they're duplicates. fill left element w/ right element
          # increment left 
          # increment k
        # otherwise, do nothing
        return k

        
