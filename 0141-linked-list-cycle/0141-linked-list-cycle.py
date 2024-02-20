# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointer technique. floyd's cycle detection
        # 1 fast pointer moves 2 times per cycle
        # slow pointer moves 1 time per cycle
        # if they're ever equal, we have detected a cycle
        fast = head
        slow = head
        while fast and fast.next:
          fast = fast.next.next
          slow = slow.next
          if fast == slow:
            return True
        return False




        