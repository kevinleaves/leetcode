# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        res = None
        curr = root
        # target is p.val => inorder successor => to the right, then to all the way to the left
        while curr:
            # curr is less or equal to target
            if curr.val <= p.val:
                # traverse right. eliminate current node
                curr = curr.right
            else:
                # if curr is > than target, our answer is potentially on this side. because we're trying to find the MIN key that's greater than p.val, we continue searching this bound to the LEFT
                res = curr
                curr = curr.left

        return res