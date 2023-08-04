# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        preorder traversal

        '''
        res = float('-inf')
        

        def findMaxPathOfNode(node):
            if not node:
                return 0

            nonlocal res
            # left, right, root
            maxPathLeft = findMaxPathOfNode(node.left)
            maxPathRight = findMaxPathOfNode(node.right)

            maxPathLeft = max(maxPathLeft, 0)
            maxPathRight = max(maxPathRight, 0)

            # update res by adding left right and currnode value
            res = max(res, node.val + maxPathLeft + maxPathRight)

            # pass up curr value + max of left and right
            return node.val + max(maxPathLeft, maxPathRight)
        
        findMaxPathOfNode(root)

        # res is the max path passing through this node?
        return res
