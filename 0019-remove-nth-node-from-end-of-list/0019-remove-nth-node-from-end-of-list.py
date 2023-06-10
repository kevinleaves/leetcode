# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1 pass using 2 pointers. slow pointer trails by n steps. once fast is completes 1 pass, slow should be at pred n node
        
        # use sentinel/dummy node because the edge case of head=[1] n = 1, which means the head can change. when the head changes, use dummy node.
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        curr = head

        # create window of n size between slow and curr
        for _ in range(n):
            curr = curr.next

        while curr:
            curr = curr.next
            slow = slow.next
        
        # slow should be at node before nth node. remove nth node
        slow.next = slow.next.next
        
        return dummy.next
        


