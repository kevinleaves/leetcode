class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # i: int
        # o: array of strings starting at 1, incrementing up until n. array is len n. 1-indexed index i of the array is "fizzbuzz" if i divisible by 3 & 5, fizz if i % 3 == 0, buzz if i % 5 == 0
        # c: none
        # e: n < 3 return [1] or [1, 2]

        res = []
        for i in range(1, n + 1):
            # append FizzBuzz
            if i % 15 == 0:
                res.append('FizzBuzz')
            # append Fizz
            elif i % 3 == 0:
                res.append('Fizz')
            # append Buzz
            elif i % 5 == 0:
                res.append('Buzz')
            # default case
            else:
                res.append(str(i))
        return res