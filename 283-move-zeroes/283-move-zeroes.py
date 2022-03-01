class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l, r = 0, len(nums)-1
        # while l <= r:
        #     if l == 0 and r != 0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         r -= 1
        #     if l!=0 and r!=0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l+=1
        #     l+=1
        # print(nums)
#         from collections import deque
        
#         arrSorted = collections.deque([])
#         for i in nums:
#             if i==0:
#                 arrSorted.append(i)
#             else:
#                 arrSorted.appendleft(i)
#         print(arrSorted)
        
        count = 0
        for i in nums:
            if i != 0:
                nums[count] = i
                count += 1
        while count < len(nums):
            nums[count] = 0
            count+=1
            