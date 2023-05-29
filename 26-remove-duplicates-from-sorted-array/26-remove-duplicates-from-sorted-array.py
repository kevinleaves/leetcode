class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # init count variable
        count = 1
        # init pointer j that stays at the next spot to be overwritten
        j = 1
        # use i to iterate over the input nums array starting from the second element
        for i in range(1, len(nums)):
            # if the number at pointer i is the same as the last number, we increment count
            if nums[i] == nums[i - 1]:
                count += 1
            # if it isn't, we know we're at a new number, reset count
            else:
                count = 1
            # at every iteration, check to see if the count is == 1. if count is 1, that means we're at a valid subarray value and we can fill in the subarray and increment j
            if count == 1:
                nums[j] = nums[i]
                j += 1
        # by the end of the algorithm, j will be the length of the new array w/ removed duplicates
        return j
