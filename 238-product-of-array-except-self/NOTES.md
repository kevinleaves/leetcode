​class Solution:
def productExceptSelf(self, nums: List[int]) -> List[int]: # i: int array nums. # o: array such that answer[i] is equal to the product of all the elements in nums except answer[i]. array length is == to nums array # c: O(n) time, without using division operation # e:

        # make an array res that's equal to the length of the initial array nums


        # initiate a running prefix total


        # iterate using i: i starts at 0 and ends at length of nums


            # result array at ith index = prefix


            # update running prefix total by multiplying it by the current number in the iteration
            prefix *= nums[i]

        # initiate a running postfix total
        postfix = 1

        # iterate backwards over nums. i starts at length of array - 1, ends at -1.
        for i in range(len(nums) - 1, -1, -1):

            # result array at ith index is equal to itself * postfix. we do this because we already calculated the postfix and don't want to overwrite the results of the first iteration.
            res[i] *= postfix

            # update running postfix to be equal to itself times the current number
            postfix *= nums[i]

        return res
