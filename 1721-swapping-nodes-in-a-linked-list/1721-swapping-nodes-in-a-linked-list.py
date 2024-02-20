# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      # key: swap nodes doesn't necessarily mean swap pointers
      # can swap values
      # find references to the correct nodes and swap them

      dummy = ListNode(None, head)
      n = 0 # n is the length of the list
      curr = head
      while curr:
        n += 1
        curr = curr.next
      
      # 0 based indices of the target nodes
      left_pointer = k - 1
      right_pointer = n - k

      leftNode = None
      rightNode = None

      curr = head
      for _ in range(0, left_pointer):
        curr = curr.next
      leftNode = curr

      curr = head
      for _ in range(0, right_pointer):
        curr = curr.next
      rightNode = curr

      leftNode.val, rightNode.val = rightNode.val, leftNode.val
      return dummy.next
      





