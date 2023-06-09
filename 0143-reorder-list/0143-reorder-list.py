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
        # find mid node
        fast = head
        mid = head
        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next
        
        # reverse right portion of list
        tail = None
        curr = mid
        while curr:
            next = curr.next
            curr.next = tail
            tail = curr
            curr = next

        # build new linked list
        curr = head
        while tail and tail.next:
            # store next nodes from left and right and change the pointers
            rightNext = curr.next # 2
            curr.next = tail # 1 -> 5
            leftNext = tail.next # 4
            tail.next = rightNext # 5 -> 2
            
            # traverse towards center
            curr = rightNext
            tail = leftNext
        
        return head


