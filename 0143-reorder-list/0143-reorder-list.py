# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # [1,2,3,4,5,6,7] -> [1,7,2,6,3,5,4]
        # find midpoint, reverse right side of list
        dummy = ListNode(None, head)
        curr = head
        mid = head

        # in odd numbered lists, the tail is in the right spot
        # but in even numbered lists, the tail points to None
        while curr and curr.next:
          curr = curr.next.next
          mid = mid.next

        # reverse right side of list using mid node as head
        
        prev = None
        curr = mid
        while curr:
          tmp = curr.next
          curr.next = prev
          prev = curr
          curr = tmp

        curr = head
        # prev is tail
        while prev and prev.next:
          rightNext = curr.next
          leftNext = prev.next
          curr.next = prev
          prev.next = rightNext

          curr = rightNext
          prev = leftNext
        return dummy.next

          
          


        




