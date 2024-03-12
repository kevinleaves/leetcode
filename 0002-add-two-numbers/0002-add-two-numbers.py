# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> [ListNode, int]:
      curr = head
      prev = None
      n = 0
      while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
        n += 1
      return [prev, n]

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        reverse both lists, while maintaining the length of both lists
        use both list n's to convert list to an int
        add ints together
        split the int into a linked list
        reverse that list and return it
        '''
        l1, n1 = self.reverseList(l1)
        l2, n2 = self.reverseList(l2)
        sum1 = 0
        sum2 = 0

        curr1 = l1
        while curr1:
          sum1 += curr1.val * (10 ** (n1-1))
          n1 -= 1
          curr1 = curr1.next

        curr2 = l2
        while curr2:
          sum2 += curr2.val * (10 ** (n2-1))
          n2 -= 1
          curr2 = curr2.next

        resSum = sum1 + sum2
        if resSum == 0:
          return ListNode(0)
          
        dummy = ListNode()
        curr = dummy
        while resSum > 0:
          digit = resSum % 10
          curr.next = ListNode(digit)
          curr = curr.next
          resSum //= 10

        return dummy.next

        

    
