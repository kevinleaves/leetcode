class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      '''
      
      '''
      maxSubstringLength = 0
      left = 0
      right = 0
      window = {}
      while right < len(s):
      # data structure representing chars in the window
        # add char at right to window
        window[s[right]] = window.get(s[right], 0) + 1
        while window.get(s[right]) > 1:
          window[s[left]] -= 1
          left += 1
  
      # contract window if condition
        # where do i move left pointer? 
        # how do i update my data structures

      # perform check/update res
        maxSubstringLength = max(maxSubstringLength, right - left + 1)
        right += 1

      return maxSubstringLength
        