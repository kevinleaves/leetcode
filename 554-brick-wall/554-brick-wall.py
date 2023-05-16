# 16.97 6.52
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = {}

        # iterate through each row and fill in gaps. position: gapCount
        wallHeight = len(wall)
        rows = len(wall)
        for i in range(rows):
            row = wall[i]
            position = 0
            for j in range(len(row)):
                brick = row[j]
                if j is not len(row) - 1:
                    position += brick
                    gaps[position] = gaps.get(position, 0) + 1

        if len(gaps) == 0:
            return wallHeight
        else:
            return wallHeight - max(gaps.values())
