class Solution:
    def fib(self, n: int) -> int:
        # fib(n) -> fib(n - 1) + fib(n - 2)
        # fib(3) -> fib(2) + fib(1)
        # fib(2) -> fib(1) + fib(0)
        # fib(1) -> 1
        # fib(0) -> 0
        if n <= 1:
          return n
        
        return self.fib(n - 1) + self.fib(n - 2)