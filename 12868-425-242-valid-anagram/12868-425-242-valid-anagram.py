class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # edge case: s and t are different lengths
      if len(s) != len(t):
        return False

      freqS = {}
      for c in s:
        if c not in freqS:
          freqS[c] = 0    
        freqS[c] += 1
      
      for c in t:
        if c not in freqS:
          return False
        if freqS[c] == 0:
          return False
        freqS[c] -= 1
    
      return True
