class Solution:
    def prefixCheck(self, s1: str, s2: str) -> bool:
      '''
      O(M) time where M is the length of s2?

      check if s2 is a prefix of s1
      iterate through len of s2
      compare idx of s1 and s2
      if at any point they're not equal, return false
      done iterating and no return => return true
      '''
      for i in range(len(s2)):
        if i >= len(s1) or s1[i] != s2[i]:
          return False
      return True

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
      '''
      O(N * M) TIME?
      O(1) SPACE we don't use any extra memory
      
      init res to store 1-indexed index
      string split into array
      perform prefix check on each word
      if prefix check results in true, update res
      return res
      '''

      res = -1
      split = sentence.split(" ")
      for i, word in enumerate(split):
        if self.prefixCheck(word, searchWord):
          # update res
          if res == -1:
            # first encounter
            res = i + 1
          else:
            res = min(res, i + 1)

      return res
    
