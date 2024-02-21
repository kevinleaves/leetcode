class Solution:
    def pivotInteger(self, n: int) -> int:
        '''
        i: int n
        o: pivot int x. x is an int where sum([1...x] ) == sum(x...n) all inclusive. if no such int exists, return -1. 
        c: no time/space constraints 
        e: n is >= 1.
        '''

        leftSum = 0
        rightSum = sum(range(1,n+1))
        for x in range(1, n+1):
          # update leftSum
          leftSum += x

          # compare the two
          if leftSum == rightSum:
            return x

          # update rightSum
          rightSum -= x

        return -1
