class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        '''
        i: int[] nums
        o: int
        c: none
        e: 0 is not in the array. n

        number line
        how many times does the ant land directly back to 0. it starts at 0  
        '''

        count = 0
        position = 0
        # iteration over nums
        for num in nums:
          # add current num to position
          position += num
          # if position 0
          if position == 0:
            # increment count
            count += 1

        return count


