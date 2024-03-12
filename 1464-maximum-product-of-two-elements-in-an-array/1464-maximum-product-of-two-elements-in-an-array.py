class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        brute force check pairs and store a max product
        O(N^2) TIME
        O(1) SPACE
        '''
        res = (nums[0]-1) * (nums[1]-1)
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
            res = max(res, (nums[i]-1) * (nums[j]-1))

        return res