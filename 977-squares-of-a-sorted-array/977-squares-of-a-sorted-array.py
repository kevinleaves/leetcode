class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1 

        result = [0]*len(nums)
        read_pointer = len(nums)-1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result[read_pointer] = nums[l]**2
                l+=1
            else: #abs(nums[l]) < abs(nums[r]):
                result[read_pointer] = nums[r]**2
                r-=1
            read_pointer-=1
            print(read_pointer)
        return result