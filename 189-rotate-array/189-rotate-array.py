class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #left and right pointers
#         nums = nums[::-1]
#         print(nums)
#         n = len(nums)-1
        
#         subarray1 = nums[:k]
#         subarray2 = nums[k:]
#         print(subarray1, subarray2)
        
#         subarray1 = subarray1[::-1]
#         subarray2 = subarray2[::-1]
#         print(subarray1+subarray2)
        
        #do the above but with 2 pointers instead
        k = k % len(nums)
        
        l, r = 0, len(nums)-1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        #reverse sublist1 (up to k elements) nums[:k]
        l, r = 0, k-1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        
        #reverse sublist2 (k onwards) nums[k:]
        l, r = k, len(nums)-1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        