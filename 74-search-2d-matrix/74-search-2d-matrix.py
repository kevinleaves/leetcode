class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bsearch(row, target):
            l, r = 0, len(row) - 1
            while l <= r:
                mid = (r + l) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        # find correct row to bsearch
        up, down = 0, len(matrix) - 1

        while up <= down:
            mid = (up + down) // 2
            # is target within mid boundary? if so run bsearch
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                # even if target isn't ultimately in the matrix, still returns false. slightly inefficient tho
                return bsearch(matrix[mid], target)
            elif target <= matrix[mid][0] and target <= matrix[mid][-1]:
                # chop upper row
                down = mid - 1
            else:
                # chop lower row
                up = mid + 1
