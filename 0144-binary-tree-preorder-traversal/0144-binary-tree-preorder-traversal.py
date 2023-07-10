# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      '''
      iterative dfs (simulate recursion)
      add, left, right
      '''
      res = []
      stack = []
      # use a pointer to emulate recursive tree traversal
      curr = root

      while curr or stack:
        # traverse left but add right node first
        if curr:
          res.append(curr.val)
          stack.append(curr.right)
          curr = curr.left
        else:
          curr = stack.pop()
        
      return res


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
      '''