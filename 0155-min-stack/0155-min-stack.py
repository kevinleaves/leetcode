# constraints -> all operations have to run at O(1) time

class MinStack:
    # attributes
    def __init__(self):
      self.data = []
      self.min = float('inf')
      
    def push(self, val: int) -> None:
      # update min if necessary
      if val < self.min:
        self.min = val
        
      # append tuple of val and min at this timestamp
      self.data.append((val, self.min))

    def pop(self) -> None:
      popped = self.data.pop()
      # we could have popped the min value from the stack. 
      if self.min == popped[0]:
        # if at least 1 item in the stack, update min with new top min
        if len(self.data) > 0:
          self.min = self.data[-1][1]
        else:
        # otherwise stack is empty, set min to infinity again
          self.min = float('inf')

    def top(self) -> int:
      return self.data[-1][0]  

    def getMin(self) -> int:
      return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()