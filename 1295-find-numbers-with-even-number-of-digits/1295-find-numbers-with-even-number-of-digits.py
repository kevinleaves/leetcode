class Solution:
    def findNumbers(self, nums: List[int]) -> int:
    
      
      def findNumberDigits(number: int):
        count = 0
        while number > 0:
          number //= 10
          count += 1
        return count
      
      count = 0
      for num in nums:
        if findNumberDigits(num) % 2 == 0:
          count += 1
          
      return count