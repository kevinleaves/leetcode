# 16.92% 6.45%
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


# FAILED ATTEMPT. OVERCOMPLICATED THINGS & USED A DICT TO INSTANTIATE. can probably make this work tho. same concept applies
class MinStack:
    def __init__(self):
        self.data = {}
        # store k:v pair for the min value in stack. update this array as we push. lookup
        self.min = []
        self.index = 0

    def push(self, val: int) -> None:
        # return nothing
        self.data[self.index] = val

        # update min
        if not self.min:
            self.min.append(self.index)
            self.min.append(val)
        else:
            if val < self.min[1]:
                self.min[0] = self.index
                self.min[1] = val

        # update index
        self.index += 1

    def pop(self) -> None:
        # return nothing
        self.index -= 1
        popped = self.data[self.index]
        del self.data[self.index]
        # if i deleted the minimum, update the val
        # if popped == self.min[1]:

    def top(self) -> int:
        # return int
        return self.data[self.index - 1]

    def getMin(self) -> int:
        # return int
        return self.min[1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
