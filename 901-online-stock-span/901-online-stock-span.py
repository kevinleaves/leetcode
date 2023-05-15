# 92.79% 11.15%
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # store price/span pairs in stack
        # before we add pair to stack we check if price < top of stack. if so add price:1 return 1
        if self.stack and price < self.stack[-1][0]:
            self.stack.append((price, 1))
            return 1
        # if price >= top of stack,
        # while iteration to pop top of stack
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            popped = self.stack.pop()
            span += popped[1]
            # with every successful pop, increment current price's span by amt of the popped span
        # add price:span to top of stack
        self.stack.append((price, span))
        # return top stack span
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
