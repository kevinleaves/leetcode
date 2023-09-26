# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        instantiate prev pointer to null (this will help us reverse the links)
        while head is not null
            store reference to next node before we reverse the link
            reverse the link by setting head.next to prev
            move prev to head
            move head to next
        return prev
        '''
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev