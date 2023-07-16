# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        res = []
        def dfs(node):
            if not node:
                return None
            
            # left, node, right
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return res
        '''
        res = []
        stack = []
        curr = root

        while curr or stack:
            # add right nodes to stack
            # traverse all the way left
            while curr:
                # add current node and all left nodes to the stack
                stack.append(curr)
                curr = curr.left
            
            # once we've hit our base case, pop node, process, go right
            node = stack.pop()
            res.append(node.val)
            curr = node.right

        return res