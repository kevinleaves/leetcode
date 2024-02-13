class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # quadratic time, constant space TLE
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        
        # set constructor accepts an iterable
        # linear space, linear time
        # res = set(nums)
        # return not (len(res) == len(nums))
        
        nums.sort()
        for i in range(len(nums)):
            if i != len(nums)-1: # if i isn't the last index
                if nums[i] == nums[i + 1]:
                    return True
        return False