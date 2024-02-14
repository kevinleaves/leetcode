class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # do not use modulo because 6 is not a power of 2
        # truth/base case
        # 1 is the smallest power of 2

        if n == 1:
          return True 
          
        if n <= 0:
          return False
        
        if n % 2 == 1:
          return False
        
        return self.isPowerOfTwo(n//2)
        
        



