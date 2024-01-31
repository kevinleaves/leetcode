# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # sentinel node/dummy node becomes the new tail
        # floating next reference to the next node
        # traverse initial order while simultaneously reversing the links

        # need a prev node
        # iterate through current list starting from the head (iteration stops when curr node is null)
          # store reference to next node
          # set current node's next to the node behind it
          # current node becomes next node that we stored a reference to earlier

        prev = None
        curr = head
        while curr:
          next = curr.next
          curr.next = prev
          prev = curr
          curr = next
        
        return prev

        

