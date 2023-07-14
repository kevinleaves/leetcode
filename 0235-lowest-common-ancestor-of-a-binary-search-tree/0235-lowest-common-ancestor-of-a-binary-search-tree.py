# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        i: BST, p & q nodes
        o: LCA node
        c: none
        e: idk
        '''
        if not root:
            return None

        if p.val > root.val and q.val > root.val:
            # recursively traverse right
            root = self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            root = self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

        return root

        