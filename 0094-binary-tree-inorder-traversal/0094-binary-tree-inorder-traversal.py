# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        # emulate recursion iteratively using a stack & pointer
        curr = root
        while curr or stack:
            # traverse left until we hit null
            while curr:
                stack.append(curr)
                curr = curr.left
            # pop to return which means we add nodes as we traverse left
            node = stack.pop()
            res.append(node.val)
            
            # processed left => attempt right
            curr = node.right

        return res