class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(N) space, O(N) time
        prefixes = [0]*len(nums)
        runningPrefixProduct = 1
        for i, num in enumerate(nums):
          # update prefix array
          prefixes[i] = runningPrefixProduct
          # update runningProduct
          runningPrefixProduct *= num

        runningSuffixProduct = 1
        for j in range(len(nums) - 1, -1,-1):
          prefixes[j] *= runningSuffixProduct
          runningSuffixProduct *= nums[j]

        return prefixes
        