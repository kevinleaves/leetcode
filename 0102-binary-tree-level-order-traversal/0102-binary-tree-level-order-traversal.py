# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        level order traversal is bfs
        q 
        add all nodes of a level to q
        process (add node into subarray)
        once we're done with a level, push into res array

        res = [[3]]
        q [[9], [20]]
        node = [3]
        '''
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            
            res.append(level)

        return res

