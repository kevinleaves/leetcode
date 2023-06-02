# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 48.82% 31.92% surprisingly efficient solution. we can improve the space here if we don't build an external array. can we optimize this to be O(1) space? it's already O(n) time. 1 pass through the initial linked list and 1 pass through the created array to reverse it is O(2n) => O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # traverse through linked list, build an array from the linked list values
        # use array of values to compute boolean
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res[::-1] == res
