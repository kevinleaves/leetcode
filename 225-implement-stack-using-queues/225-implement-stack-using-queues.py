class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        return

    def pop(self) -> int:
        # keep popping from left + add back to right until the farright element is at the farleft
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        # done with the pops, now the element that should be returned is on the very left.
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
