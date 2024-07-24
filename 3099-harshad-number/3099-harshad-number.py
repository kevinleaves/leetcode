class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # find sum of digits (in a math way)
        sumOfDigits = 0
        n = x
        while n > 0:
          lastDigit = n % 10
          sumOfDigits += lastDigit
          n -= lastDigit
          n /= 10

        return int(sumOfDigits) if x % int(sumOfDigits) == 0 else -1
        
        # x % sum == 0, return sum, otherwise return -1