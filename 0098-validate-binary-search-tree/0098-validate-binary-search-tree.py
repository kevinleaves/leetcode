# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        set a min, max range
        update values as we traverse left and right
        if we traverse left, update upper bound
        if we traverse right, update min bound
        init bounds as 
        '''

        lower, upper = float('-inf'), float('inf')
        def isValid(node: Optional[TreeNode], lower, upper) -> bool:
            if not node:
                return True
            
            # check if node is within range?
            if node.val >= upper or node.val <= lower:
                return False

            # traverse left, update upper
            left = isValid(node.left, lower, node.val)
            
            # traverse right, update lower
            right = isValid(node.right, node.val, upper)

            return left and right


        return isValid(root, lower, upper)
        