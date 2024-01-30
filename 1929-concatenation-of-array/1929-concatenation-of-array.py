class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create new array of size 2n
        n = len(nums)
        res = [0] * (2 * n)

        # iterate through nums, fill new array 2 slots at a time
        for i in range(n):
          res[i] = nums[i]
          res[i + n] = nums[i]
  
        # return new array
        return res