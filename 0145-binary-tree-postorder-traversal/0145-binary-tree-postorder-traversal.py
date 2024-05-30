# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      res = []
      # postorder used when parent node needs the results of children node to compute its result
      def dfs(node: Optional[TreeNode]) -> None:
        if not node:
          return None
        
        # left
        dfs(node.left)
        # right
        dfs(node.right)
        # process
        res.append(node.val)
      
      dfs(root)
      return res
        