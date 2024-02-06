# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
          return 0
        
        res = 1
        q = collections.deque()
        q.appendleft(root)
        
        while q:
          # update depth when we successfully increase a level
          for _ in range(len(q)):
            curr = q.popleft()
          # we've encountered a leaf when a node has null left and right
            if not curr.left and not curr.right:
              return res
          # process nodes
            if curr.left:
              q.append(curr.left)
            if curr.right:
              q.append(curr.right)

          res += 1
        # only update the depth when it's valid, or when we reach a node with no children (a leaf)
        # find valid depth

        # return min depth
        return res