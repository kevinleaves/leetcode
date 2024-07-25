class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
      '''
      i: 2d sorted grid in descending order both ways
      o: int (# of negative numbers in the matrix)
      c: o(n + m) time optimal
      e: 

      m num rows
      n num of columns

      brute force is n x m time because i hit every element
      
      [
      [4,3,2,-1],
      [3,2,1,-1],
      [1,1,-1,-2],
      [-1,-1,-2,-3]
      ]
      [3, 2]
      [1, 0]
      bottom left traversal upwards and to the right
      col bounds: cIdx < number of cols
      row bounds: rIdx > -1

      if current number is negative, all columns to the right are also negative, add these to the count
        then move up 1 row  because we're done traversing current row's columns
      otherwise
        increment col to the right and check there
      '''
      res = 0
      r = len(grid)
      c = len(grid[0])
      
      # starting point is bottom left
      rIdx = r - 1
      cIdx = 0

      # `and` because we need both to be in-bounds in order to traverse
      while rIdx > -1 and cIdx < c:
        if grid[rIdx][cIdx] < 0:
          res += c - cIdx
          rIdx -= 1
        else:
          cIdx += 1

      return res

      
      



