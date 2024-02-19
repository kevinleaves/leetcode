# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # delete a node without reference to any previous nodes
        # do not need to return value of the deleted node
        # pull forward value of next node, set curr value to the pulled value
        node.val = node.next.val
        node.next = node.next.next
        

        


        