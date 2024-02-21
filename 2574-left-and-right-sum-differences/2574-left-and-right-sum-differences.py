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
        
        # time complexity n^3?
        for i in range(len(nums)):
          leftSum = 0
          rightSum = 0
          # update leftSum
          for j in range(i):
            leftSum += nums[j]
          
          # update rightSum
          for j in range(i + 1, len(nums)):
            rightSum += nums[j]

          # set res at i
          res[i] = abs(leftSum - rightSum)

        return res