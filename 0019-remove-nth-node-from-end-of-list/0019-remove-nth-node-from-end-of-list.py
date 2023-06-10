# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # brute force, multiple passes
        # find size of LL with 1 pass
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        # if 1 node, remove it and return None
        if size == 1:
            return None

        curr = head
        prev = None
        # reset curr and prev, move curr size - n times so curr is at n and prev is 1 node trailing.
        for _ in range(size - n):
            prev = curr
            curr = curr.next

        # make prev point to curr.next
        if prev:
            prev.next = curr.next
        else:
            head = head.next    
        # if curr is already at the nth node, remove it
        
        # return head
        return head