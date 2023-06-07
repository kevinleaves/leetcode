# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # store B nodes in a set
        seenB = set()
        currB = headB
        while currB:
            seenB.add(currB)
            currB = currB.next
        
        # iterate through headA to check for inclusion of A nodes in B. if there are any, we have an intersection, return the node.
        currA = headA
        while currA:
            if currA in seenB:
                return currA
            currA = currA.next
            
        return None