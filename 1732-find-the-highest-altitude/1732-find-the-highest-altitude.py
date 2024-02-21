class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        '''
        i: int[] gain. length n. road trip is n+1 length
        o:
      
        [-5, 1, 5, 0,-7]
        altitude[] altitude[i] = prefix sum of the gain[i]
        [0, -5,-4, 1, 1, -6]
        
        goal: calculate a altitude array and record the max value in this array
        '''
        maxAltitude = 0
        leftSum = 0
        for i in range(len(gain)):
          leftSum += gain[i]
          maxAltitude = max(leftSum, maxAltitude)
        return maxAltitude


