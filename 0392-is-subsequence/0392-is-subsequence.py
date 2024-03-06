class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      '''
      use 2 pointers, one at s and one at t
      iterate through t pointer
        attempt to find the character at s pointer in t
        once we've found a character at t,
        increment t
      
      if we've reached the end of t and have not yet exhausted s pointer, return False
      otherwise return true

      '''
      # edge cases. s is empty, return true
      # t is empty, return false
      if len(s) == 0:
        return True
      if len(t) == 0:
        return False

      s_index = 0
      for t_index in range(len(t)):
        if s_index == len(s):
          return True
        if t[t_index] == s[s_index]:
          s_index += 1
      
      return False if s_index < len(s) else True