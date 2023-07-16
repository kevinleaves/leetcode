# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        base case(s)
        both nodes are null
        '''
        # both nodes do not exist
        if not root1 and not root2:
            return None

        # 1 node exists but not the other. treat a null node as 0
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        # create a new node from the merged values
        mergedNode = TreeNode(v1 + v2)

        left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        # link the subtrees together
        mergedNode.left = left
        mergedNode.right = right

        return mergedNode