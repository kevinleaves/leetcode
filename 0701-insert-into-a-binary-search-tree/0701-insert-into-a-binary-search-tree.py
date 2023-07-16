# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # base case returns the newly created node
        if not root:
            return TreeNode(val)
        # check for left/right traversal
        
        if val > root.val:
            right = self.insertIntoBST(root.right if root else None, val)
            root.right = right
        elif val < root.val:
            left = self.insertIntoBST(root.left if root else None, val)
            root.left = left
        return root
