# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        regular solution
        reverse second half of ll
        fast and slow pointer
        slow pointer will always end up as the head of the 2nd part of the list
        reverse the list to the right of this head

        iterate thru ll from right side until it reaches null. 
        we don't have to deal with breaking the link from the first head to the 2nd list head

        traverse both heads at the same time, updating res as we go
        '''
        fast = head
        slow = head
        while fast:
          fast = fast.next.next
          slow = slow.next
        
        prev = None
        curr = slow
        while curr:
          tmp = curr.next
          curr.next = prev
          prev = curr
          curr = tmp
        
        curr = prev

        res = 0
        while curr:
          res = max(res, head.val + curr.val)
          curr = curr.next
          head = head.next

        return res



        

