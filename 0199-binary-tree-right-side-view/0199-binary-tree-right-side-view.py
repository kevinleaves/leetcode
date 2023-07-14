# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        i: root of btree
        o: array w/ ints that you can see from the right side
        c: none
        e: empty root
        '''

        if not root:
            return None
        
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            qLen = len(q)
            # bfs iterating through 1 level at a time
            for i in range(qLen):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == qLen-1:
                    res.append(node.val)

        return res
        '''
        res = []
        q: [15, 5, 4]
        '''