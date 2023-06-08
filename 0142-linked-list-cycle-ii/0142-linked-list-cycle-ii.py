# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(N) time + space. iterate through entire N nodes, store N nodes in set
        # store nodes in set
        seen = set()
        # iterate through LL, if we've seen the node before, we're at the beginning, return that node
        curr = head
        while curr:
            if curr in seen:
                return curr
            else:
                seen.add(curr)
                curr = curr.next
        
        # otherwise no cycles, return None
        return None