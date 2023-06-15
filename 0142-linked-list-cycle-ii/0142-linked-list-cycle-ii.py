# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find intersection node using floyd's
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # save ref to intersection node
                # init pointer at head again
                slow2 = head
                while slow2:
                    if slow2 == slow:
                        return slow2    
                    slow2 = slow2.next
                    slow = slow.next
                # traverse until pointer == intersection node

        # if no intersection, return -1
        return None
        