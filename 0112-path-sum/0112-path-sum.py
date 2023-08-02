# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def inorder(root, pathSum):
            if not root:
                return None

            if not root.left and not root.right:
                if pathSum + root.val == targetSum:
                    return True

            left = inorder(root.left, pathSum + root.val)

            right = inorder(root.right, pathSum + root.val)

            return left or right

        return inorder(root, 0)

            
        