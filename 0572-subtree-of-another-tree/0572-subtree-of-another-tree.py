# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            
            left = sameTree(s.left, t.left)
            right = sameTree(s.right, t.right)
            return left and right
        
        # base case(s)
        if not root:
            return False
        if not subRoot:
            return True

        res = sameTree(root, subRoot)

        if not res:
            # recursive case(s)
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right
        else:
            return True


        
