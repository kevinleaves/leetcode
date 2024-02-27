class ListNode:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
      self.capacity = k
      self.size = 0
      self.front = self.rear = ListNode()
      
    def enQueue(self, value: int) -> bool:
      # check if list is full. early return if operation not possible
      flag = True
      if self.size + 1 > self.capacity:
        flag = False
        return flag

      # create new node
      node = ListNode(value)
      # enqueue to empty list
      self.rear.next = node
      self.rear = node
      self.size += 1
      # not empty list
      return flag

    def deQueue(self) -> bool:
      flag = True
      if self.isEmpty():
        flag = False
        return flag

      # remove from head
      tmp = self.front.next
      self.front.next = self.front.next.next
      tmp.next = None
      if self.front.next == None:
        self.rear = self.front
      self.size -= 1
      return flag

    def Front(self) -> int:
      if self.isEmpty():
        return -1
      return self.front.next.val    

    def Rear(self) -> int:
      if self.isEmpty():
        return -1
      return self.rear.val

    def isEmpty(self) -> bool:
      return self.size == 0  

    def isFull(self) -> bool:
      return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()