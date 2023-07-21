# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal of bst        
        # iterative: we don't have to traverse entire bst, we stop when we reach k
        
        stack = []
        curr = root
        position = 1

        while curr or stack:
            # traverse left
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            # action with node
            if position == k:
                return node.val
            else:
                position += 1

            # traverse right
            curr = node.right


