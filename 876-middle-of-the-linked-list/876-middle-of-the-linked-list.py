# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        #fast works if list is even 
        #fast.next works if list is odd 
        #we use both conditions in our while statement to catch both scenarios
        while (fast and fast.next): 
            slow = slow.next
            fast = fast.next.next
        return slow
            