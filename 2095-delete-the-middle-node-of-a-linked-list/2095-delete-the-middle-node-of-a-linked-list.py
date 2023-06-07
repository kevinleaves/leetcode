# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 81% 13.73%  11:42. 100% me
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case 1 node
        if head and not head.next:
            return None

        prev = ListNode(val=None)
        slow = head
        fast = head

        # find middle node and keep a trailing prev behind slow
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # we have prev, point its next to slow.next
        prev.next = slow.next
        return head
