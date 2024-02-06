# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # traverse 1 level/depth at a time
        res = []
        q = collections.deque()
        
        # initialize q with the root
        if root:
          q.appendleft(root)

        while q:
          # starting from the root, we add its 2 children nodes into a queue
          # level contains node values
          level = []
          # do not add null nodes to the q
          for i in range(0, len(q)):
            # process current node in the for loop
            curr = q.popleft()
            if curr.left:
              q.append(curr.left)
            if curr.right:
              q.append(curr.right)
            level.append(curr.val)
          # after we're done processing nodes aka adding child nodes to the q and adding the node val to level
          res.append(level)  
        return res