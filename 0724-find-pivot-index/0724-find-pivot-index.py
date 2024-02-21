class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''

        calculate total sum
        leftSum + nums[i] + rightSum will always equal sum(nums)

        maintain leftmost pivot index
        there can be multiple pivot indices
        '''
        
        leftSum = 0
        rightSum = sum(nums)
        for i in range(0, len(nums)):
          # update rightSum
          rightSum -= nums[i]

          # compare, update res
          if leftSum == rightSum:
            return i

          # update leftSum
          leftSum += nums[i]

        return -1

