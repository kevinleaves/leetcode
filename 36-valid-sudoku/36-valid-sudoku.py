class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row.
                if val in rows[r]: #if val is in row, return false
                    return False
                rows[r].add(val) #otherwise add it to that set

                # Check the column
                if val in cols[c]: #if val is in col, return false
                    return False
                cols[c].add(val) # otherwise add it to that set

                # Check the box
                idx = (r // 3, c // 3) # current box index
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True