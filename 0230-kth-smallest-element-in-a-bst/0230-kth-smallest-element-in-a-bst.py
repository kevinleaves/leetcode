# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal of bst to build sorted array
        # return arr[k - 1]

        res = []
        def inorder(node):
            if not node:
                return None

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        
        return res[k-1]