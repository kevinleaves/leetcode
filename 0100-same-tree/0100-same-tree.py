# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # i: 2 btree roots 
        # o: boolean representing if they're the same
        # c: none
        # e: 

        # iterative bfs
        
        # recursive dfs

        # base case:
        # 2 nodes are the same if their val is same, and they have the same l and right
        
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right



        