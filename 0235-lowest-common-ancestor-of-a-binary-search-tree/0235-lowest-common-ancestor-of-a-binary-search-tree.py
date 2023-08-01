# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''

        '''
        curr = root
        while curr:
        # curr val is above max or below min
            if curr.val > max(p.val, q.val):
                # traverse right
                curr = curr.left
            elif curr.val < min(p.val, q.val):
                curr = curr.right
            else:
                # we're either == to p or q or betwen p & q
                return curr
        
        
