class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # define res array
        res = [0]*len(nums)
        # initialize prefix product
        prefix = 1

        # pass 1
        # iterate through nums array 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # populate res
        # update prefix

        # pass 2
        # reset prefix to 1
        prefix = 1
        # iterate from right side first
        for i in range(len(nums) - 1, -1, -1):
            # populate res with current element x prefix
            res[i] *= prefix
            # update prefix (x current number)
            prefix *= nums[i] 

        # return res
        return res

        



