# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # while there are nodes in either list, continue iteration
        dummy = ListNode()
        head = dummy

        # while we haven't traversed through every node
        while list1 and list2:
          # list1 moves
          if list1.val <= list2.val:
            # append item at l1 to new head
            head.next = list1
            # move list1 curr pointer
            list1 = list1.next
          else:
            # list2 moves
            head.next = list2
            list2 = list2.next
            
          head = head.next

        # if remaining nodes in l1, add the segment to our result
        if list1:
          head.next = list1
        else:
          head.next = list2

        return dummy.next
       
