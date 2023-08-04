# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        level order traversal, take the last node of every level
        '''

        res = []
        curr = root
        q = collections.deque()
        if curr:
            q.append(curr)

        while q:
            levelLength = len(q)

            for i in range(levelLength):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == levelLength - 1:
                    res.append(node.val)
                
        return res