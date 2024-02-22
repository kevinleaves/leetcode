class Solution:
    def numberOfPoints(self, nums):
        N = 102 # number of line segments
        line = [0] * N

        for segment in nums:
            start_point, end_point = segment
            # Increment count at the start point of the segment
            line[start_point] += 1

            # Decrement count at the point after the end point of the segment
            line[end_point + 1] -= 1

        points_covered = 0 
        segment_accumulator = 0
        for count in line:            
            segment_accumulator += count            
            # if there is at least 1 segment covering the current point
            if segment_accumulator >= 1:
                points_covered += 1


        return points_covered
