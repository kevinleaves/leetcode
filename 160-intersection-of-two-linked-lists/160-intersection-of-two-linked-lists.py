# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # find last element of both lists, if they're not the same element return None
        prevA, prevB = None, None
        currA = headA
        currB = headB
        lenA, lenB = 0, 0

        while currA:
            prevA = currA
            currA = currA.next
            lenA += 1
        while currB:
            prevB = currB
            currB = currB.next
            lenB += 1

        if prevA != prevB:
            return None

        # reset pointers to initial
        currA = headA
        currB = headB

        # equalize starting points of the LL to ensure same length
        while lenA > lenB:
            currA = currA.next
            lenA -= 1
        while lenB > lenA:
            currB = currB.next
            lenB -= 1

        # if 2 nodes point to the same next, return that node
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
