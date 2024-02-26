class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        find correct write position. left needs to be pointing a zero
        right needs to be pointing at a nonzero

        swap elements
        repeat

        breaks when left >= right
        return original array

        """
        # we write at the left pointer
        write = 0
        # iterate through read pointer
        for read in range(len(nums)):
          # swap when left is a 0 and right is a nonzero
          if nums[write] == 0 and nums[read] != 0:
            nums[read], nums[write] = nums[write], nums[read]
          
          # make sure left is pointing at a 0
          if nums[write] != 0:
            write += 1
        
        

        