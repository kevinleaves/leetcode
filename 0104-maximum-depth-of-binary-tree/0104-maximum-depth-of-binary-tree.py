# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # store res which is the max depth of traversal
        res = 0

        def dfs(node, curr):
            nonlocal res

            if not node:
                return

            curr += 1
            res = max(res, curr)

            dfs(node.left, curr)
            dfs(node.right, curr)

        # recursively explore all possible paths in the tree
        # as we path, update max depth using current depth
        dfs(root, 0)

        # return max depth 
        return res
