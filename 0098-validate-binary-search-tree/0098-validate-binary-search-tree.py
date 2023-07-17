# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        helper dfs w/ upper and lower bounds
        return a boolean by checking if current node is within bounds 

        root is a bst if both its left and right subtrees are valid
        an empty tree is a valid BST

        '''

        def isWithinRange(root, low, high):
            # empty node is a BST
            if not root:
                return True

            # if node val not within range, return False
            withinRange = root.val > low and root.val < high
            if not withinRange:
                return False

            # using BST properties... if traverse left, we update upper bound
            left = isWithinRange(root.left, low, root.val)
            # using BST properties... if traverse right, we update lower bound
            right = isWithinRange(root.right, root.val, high)

            # is Valid BST when left and right
            return left and right
            
        return isWithinRange(root, float('-inf'), float('inf'))