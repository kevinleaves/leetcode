class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        '''
        i: int[]
        o: int[] same size as input
        
        abs of leftsum[i] - rightsum[i]
        at index i of result is the abs(leftsum - rightsum) where 
        leftsum is the sum of the elements to the left but not including the current element
        and rightsum is the sum of the elements to the right but not including the current element
        '''
        res = [0]*len(nums)
        leftSum = 0
        rightSum = sum(nums)


        # time complexity n^3?
        for i in range(len(nums)):
          # update sums
          rightSum -= nums[i]
          leftSum += nums[i - 1]

          # edge cases at either end of the array
          if i == 0:
            leftSum = 0  
          if i == len(nums) - 1:
            rightSum = 0

          # set res at i
          res[i] = abs(leftSum - rightSum)

        return res