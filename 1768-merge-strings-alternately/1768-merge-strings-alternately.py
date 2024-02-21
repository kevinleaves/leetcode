class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      '''
      cases: 
        w1 len == w2 len
        w1 len > w2 len
        w1 len < w2 len

      want to hit every element

      no constraints on time and space
      can build resulting string

      alternating starting with w1
      

      add w1[0]
      add w2[0]
      '''

      res = ''
      position = 0
      # outer runs as long as we haven't hit all elements
      while position < len(word1) or position < len(word2): 
        res += word1[position]
        res += word2[position]
        position += 1
        
        # w1 is longer, add the rest of w1
        if position >= len(word2):
          res += word1[position:]
          return res
        elif position >= len(word1):
        # w2 is longer
          res += word2[position:]
          return res

      return res