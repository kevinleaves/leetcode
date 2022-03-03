class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #move all 0's to the end of the array
        #OR move all nonzero to the start
        #in-place
        #2 pointers
        l = 0
        for r, value in enumerate(nums):
            if value:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                