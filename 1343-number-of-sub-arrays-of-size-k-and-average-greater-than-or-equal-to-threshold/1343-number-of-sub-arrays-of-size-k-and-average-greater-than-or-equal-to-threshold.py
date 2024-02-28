class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
      '''
      we want windows of size k that average to >= threshold
      maintain count of valid windows
      find valid window size
      return number of valid windows
      '''
      # can use a running sum of the window and divide by k to get avg
      # start with valid window length
      # move right pointer by iterating
      # move left pointer in order to make valid window. brute force search means left += 1
      # need efficient calculation of a window's average
      
      count = 0
      windowSum = 0
      left = 0  
      
      for right in range(0, len(arr)):
        windowSum += arr[right]
        # if the window is too small do nothing
        # window is too big
        if right - left + 1 > k:
          windowSum -= arr[left]
          left += 1

        # calculate when we have a valid window
        if right - left + 1 == k:
          if windowSum / k >= threshold:
            count += 1

      return count
          




