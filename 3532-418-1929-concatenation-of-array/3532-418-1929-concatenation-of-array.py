class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
      # create the static array of length 2n
      n = len(nums)
      res = [0] * (n * 2)

      for i in range(n): #0,1,2
        res[i] = nums[i]
        res[i + n] = nums[i]
      
      return res


        