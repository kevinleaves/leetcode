class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        can use extra memory
        no time constraints.
        sort?

        brute force check pairs?

        find equivalent numbers
        abs difference of indices has to be <= k
        if so return true

        return false if finished iterating and nothing found

        '''
        if k == 0:
          return False

        window = set()
        # if failed pair aka j - i > k, we don't have to compare, move on
        left = 0
        for right in range(0, len(nums)):
          # condition to update left
          if right - left > k:
            window.remove(nums[left])
            left += 1

          if nums[right] in window:
            return True
          
          window.add(nums[right])
        return False
        

        