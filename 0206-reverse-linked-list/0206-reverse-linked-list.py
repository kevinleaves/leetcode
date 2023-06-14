# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive solution
        # base case if head is 0 nodes or 1 node:
        # if head is null (0 nodes) => return head, which is null. or if 1 node (return head)
        if not head or not head.next:
            return head

        # recursive case
        # prev is the new head of the reversed sublist.
        prev = self.reverseList(head.next)

        # head.next is always the tail of our reversed sublist. reverse the pointer
        head.next.next = head

        # break the current connection
        head.next = None

        # return the new tail
        return prev