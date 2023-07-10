# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      '''
      recursive dfs
      add, left, right
      '''

      res = []
      def dfs(root):
        # base case(s)
        if not root:
          return
        # recursive case(s)
        res.append(root.val)
        dfs(root.left)
        dfs(root.right)
      
      dfs(root)
      return res
