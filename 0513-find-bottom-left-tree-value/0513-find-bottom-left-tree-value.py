# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        '''
        level = 2
        i = 1
        q = [6, 5, 4]
        '''
        res = root.val
        q = collections.deque()
        if root:
            q.append(root)
        
        while q:
            # process a level's nodes
            level = len(q)
            for i in range(level):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                if i == level - 1:
                    res = node.val

        return res
                