# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        '''
        maintain a global sum
        dfs, stop at a valid path
        process path numbers, sum them
        '''

        res = [0]

        def dfs(node, path):
            if not node:
                return 0

            path += str(node.val)
            left = dfs(node.left, path)
            right = dfs(node.right, path)
            if not left and not right:
                res[0] += int(path)
            return int(path)
            

        dfs(root, '')
        return res[0]

