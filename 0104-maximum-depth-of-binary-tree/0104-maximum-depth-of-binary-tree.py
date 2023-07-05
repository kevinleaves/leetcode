# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative BFS

        # instantiatize q
        # level is the depth we're currently at. if root is empty return 0
        q = collections.deque()
        
        level = 0 
        if root:
            q.append(root)
            
        while q:
            # iterate through a level's nodes
            for i in range(len(q)):
                # add every node at a level to the q
                node = q.popleft()
                # never add empty nodes to the q
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # once we've added to the q every node at a level, increment to next level
            level += 1
            
        return level

