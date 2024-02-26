class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:        
        nums.sort()
        minDiff = float('inf')
        left = 0
        right = k - 1
        # sorting eliminates the need to do some of the comparisons in the example
        # like we don't need to check 9 - 1 because that's obviously never the answer if it's sorted
        # sorting allows us to check contiguious windows because we're searching for the min
        # aka sorting allows us to not have to brute force check every single possible combo of k elements
        '''
        sorting allows us to only compare elements from right - left because that's the max and min of 
        subarray k
        '''
        while right < len(nums): # while right is in bounds
          currDiff = nums[right] - nums[left]
          minDiff = min(minDiff, currDiff)
          # increment pointers/slide the window
          right += 1
          left += 1

        return minDiff