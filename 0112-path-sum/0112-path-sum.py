# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currPathSum):
            if not node:
                return False
            
            currPathSum += node.val

            # is leaf, do the comparison
            if not node.left and not node.right:
                # do the comparison
                return currPathSum == targetSum

            left = dfs(node.left, currPathSum)
            right = dfs(node.right, currPathSum)

            return left or right

        return dfs(root, 0)