class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        res = 0
        for r in range(R - 2):
            for c in range(C - 2):
                start = grid[r][c]
                # find hourglass sum from starting point
                innerSum = 0
                for i in range(c, c + 3):
                    # upper row
                    innerSum += grid[r][i]
                    # lower row
                    innerSum += grid[r+2][i]
                # middle value
                innerSum += grid[r+1][c+1]
                res = max(innerSum, res)
        return res

                

