class MyStack:

    def __init__(self):
      self.q1 = collections.deque()
      self.q2 = collections.deque()

    def push(self, x: int) -> None:
      self.q1.appendleft(x)

    def pop(self) -> int:
      # pop from q1 until we get to the last element
      while len(self.q1) > 1:
        self.q2.appendleft(self.q1.pop())
      # push to back of q2 to retain order
      # final pop on q1 and return it
      res = self.q1.pop()

      # return queues back to initial state
      self.q1, self.q2 = self.q2, self.q1
      return res

    def top(self) -> int:
      # iterate through q1 to find the last element at the bottom of the queue
      i = len(self.q1) - 1
      for i in range(i, -1, -1):
        if i == 0:
          return self.q1[i]

    def empty(self) -> bool:
        return len(self.q1) + len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()