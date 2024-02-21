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

        leftSum = 0
        rightSum = 0
        res = [0]*len(nums)
        
        for i in range(len(nums)):
          # update leftSum
          leftSum = sum(nums[:i])
          # update rightSum
          rightSum = sum(nums[i+1:])

          # set res at i
          res[i] = abs(leftSum - rightSum)

        return res