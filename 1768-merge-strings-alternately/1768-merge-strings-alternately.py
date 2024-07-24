class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # happy path -> both words are equal length
        s = ''
        if len(word1) == len(word2):
          for i in range(len(word1)):
            s += word1[i]
            s += word2[i]
          return s

        # unhappy path -> words are != length
        if len(word1) < len(word2):
          i = 0
          while i < len(word1):
            s += word1[i]
            s += word2[i]
            i += 1
          s += word2[i:]
          return s

        if len(word1) > len(word2):
          i = 0
          while i < len(word2):
            s += word1[i]
            s += word2[i]
            i += 1
          s += word1[i:]
          return s
