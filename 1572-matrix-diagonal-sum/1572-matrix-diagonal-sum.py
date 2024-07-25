class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
      r = len(mat)
      c = len(mat[0])

      isOddMatrix = len(mat) % 2 == 1

      rIdx = 0 #top left
      cIdx = 0 #top left

      d1 = 0
      d2 = 0
      
      # primary diagonal l -> r
      while rIdx < r and cIdx < c:
        d1 += mat[rIdx][cIdx]
        rIdx += 1
        cIdx += 1

      # secondary diagonal r -> l
      rIdx = 0
      cIdx = c - 1

      while rIdx < r and cIdx > -1:
        d2 += mat[rIdx][cIdx]
        rIdx += 1
        cIdx -= 1
      
      res = d1 + d2 if not isOddMatrix else d1 + d2 - mat[r//2][c//2]

      return res