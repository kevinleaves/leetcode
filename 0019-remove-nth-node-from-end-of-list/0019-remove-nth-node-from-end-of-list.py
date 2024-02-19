# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # header node
        header = ListNode(None, head)
        # remove node from the back without a reference to the tail node
        '''
        solution 1: any # of passes
        # find length of list k
        # remove the (k - n)th node from the front

        handle the remove 0th node edge case
        '''
        # iterate 1 time, counting the number of elements in the list, k
        # target index to remove is index k - n
        # iterate until curr pointer is at element prior to the removed element
        # shift that pointer to the k-n th's node.next
        k = 0
        curr = head
        while curr:
          k += 1
          curr = curr.next
        
        target = k - n
        if target == 0:
          header.next = header.next.next
          return header.next

        curr = head
        for _ in range(0, target - 1):
          curr = curr.next
        
        curr.next = curr.next.next
        return header.next


        