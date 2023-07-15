# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        '''
        starting at the root dfs to traverse both trees simultaneously. if ever their values are !=, return false upwards. if any falses, return false
        '''
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        # compare them
        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right

    
        