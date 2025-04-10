class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      ref = strs[0]
      # iterate through possible indices
      res = ""
      for i in range(len(ref)):
        for s in strs:
          if i == len(s):
            return res
          if s[i] != ref[i]:
            return res
        res += s[i]
      
      return res
