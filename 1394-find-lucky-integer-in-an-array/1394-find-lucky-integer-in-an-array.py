class Solution:
    def findLucky(self, arr: List[int]) -> int:
      # O(N) time
      # O(N) space
        
      freq = {}
      for num in arr:
        freq[num] = freq.get(num, 0) + 1

      res = -1
      for key in freq:
        if freq[key] == key:
          # we have a lucky number
          res = max(res, key)

      return res