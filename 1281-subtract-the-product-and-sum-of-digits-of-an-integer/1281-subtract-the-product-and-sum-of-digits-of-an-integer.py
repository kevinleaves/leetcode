# 30.99%  13.32%
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []

        def recurse(n):
            # base case
            if n <= 0:
                return

            # recursive case
            digit = n % 10
            n -= digit
            n /= 10
            digits.append(digit)
            recurse(n)

        recurse(n)

        def calcProductOfArray(array):
            product = 1
            for number in array:
                product *= number
            return int(product)

        return calcProductOfArray(digits) - int(sum(digits))
