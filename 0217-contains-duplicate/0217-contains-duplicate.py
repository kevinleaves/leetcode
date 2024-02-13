class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # quadratic time, constant space TLE
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        
        res = set(nums)
        return not (len(res) == len(nums))