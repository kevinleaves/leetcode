class MinStack:
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        # each node of the stack is a tuple: (val, min_value_at_that_point)
        # so when we pop the min most value up to that point, we're chillin and always have access to the min value at any node

        # this covers the first push to an empty stack
        if not self.data:
            self.data.append((val, val))
            return

        topTuple = self.data[-1]
        currMin = topTuple[1]
        self.data.append((val, min(val, currMin)))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
