class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # no good substrings if initial string length is < 3
        if len(s) < 3:
          return 0

        l = 0
        r = 2
        # brute force check every substring of len 3
        count = 0
        while r < len(s):
          # take substring convert it to a set
          # if it's len 3, increment count
          if len(set(s[l:r+1])) == 3:
            count += 1
          l += 1
          r += 1

        return count

