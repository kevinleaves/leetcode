class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = 0
        # for i in nums:
        #     if i != 0:
        #         nums[count] = i
        #         count += 1
        # while count < len(nums):
        #     nums[count] = 0
        #     count+=1

            
        l = 0
        #move all nonzero values to the left
        for r in range(0, len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                
            