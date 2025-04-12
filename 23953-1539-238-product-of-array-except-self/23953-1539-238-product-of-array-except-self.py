class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      # brute force O(n^2) time
      # res = []
      # for i in range(len(nums)):
      #   product = 1
      #   for j in range(len(nums)):
      #     if i != j:
      #       product *= nums[j]
      #   res.append(product)
      # return res

      prefixArray = [0]*len(nums)
      # populate prefix array so at each index is the proudct of all numbers
      # before it
      product = 1
      for i, n in enumerate(nums):
        prefixArray[i] = product
        product *= n

      # do suffixes
      suffixArray = [0]*len(nums)
      product = 1
      for i in range(len(nums) - 1, -1, -1):
        suffixArray[i] = product
        product *= nums[i]

      res = [0]*len(nums) # res is the result of prefix * suffix at each index
      for i in range(len(nums)):
        res[i] = prefixArray[i] * suffixArray[i]
      return res

