class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    l = 0
    r = k
    maxSum = sum(nums[:k])
    currSum = maxSum
    
    while l <= r and r < len(nums): 
      if r - l + 1 > k:
        currSum -= nums[l]
        l += 1
      
      currSum += nums[r]
      maxSum = max(currSum, maxSum)
      r += 1
    return maxSum / k
        
    # expand window to the right
    # if window size is > k, contract window by incrementing l
    # create valid window of size k
    # once we have a valid window size:
      # find avg of window & store it
      # update if curr avg > max avg

    # return max avg
        
