# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # i: root of btree
        # o: int representing diameter of tree (length of longest path between any 2 nodes)
        # c: none
        # e: empty tree?

        # establish global result variable
        res = 0
        
        # base case
        def dfs(node):
            if not node:
                return 0
            # nonlocal allows us to access & modify outer closure variable
            nonlocal res

            # recursive case
            left = dfs(node.left) # 0
            right = dfs(node.right) # 0

            # update res. diameter is equal #ofrightedges + #ofleftedges
            res = max(res, left + right)
            
            # +1 accounts for the edge connecting the node to parent
            return max(left, right) + 1        
        
        dfs(root)
        return res
