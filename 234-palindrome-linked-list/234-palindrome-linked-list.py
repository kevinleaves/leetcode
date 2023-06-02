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


# 93.9% 61.94%
# key to this solution: find the midpoint node using fast/slow algorithm. reverse the LL starting from that point to find the tail. use head and tail to check for palindrome. remember that when you reverse the rightmost portion of the linked list, the midpoint points to a Null previous node, so that is the condition for when your palindrome check loop ends.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # traverse through linked list, build an array from the linked list values
        # use array of values to compute boolean
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # we've found the middle, reverse back half of LL
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # prev is now pointing towards our tail. is flowing <-
        # while loop comparing values at both ends. check for palindrome
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
