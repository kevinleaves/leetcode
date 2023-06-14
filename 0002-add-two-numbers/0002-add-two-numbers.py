# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        # continue loop until we've traversed l1 and l2 fully and until carry is 0
        while l1 or l2 or carry == 1:
            # if else conditions handle edge case of numbers having mismatching digits
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # elementary school math
            sum = x + y + carry

            # calculate a new carry value for the next iteration (could be 0 or 1)
            carry = sum // 10
            
            # make a new node, calculated from the summed value
            curr.next = ListNode(sum % 10)

            # advance l1 & l2 pointers if the nodes exist, otherwise they're Null
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
            curr = curr.next
        return dummy.next
            

            