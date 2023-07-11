# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
        i: root node
        o: boolean
        c: no time/space constraints. no recursive/iterative constraints
        e: 
        """
        
        def dfs(node):
            # base case(s)
            if not node:
                return (True, 0)
            
            # recursive case(s)
            left = dfs(node.left) # (True, 0)
            right = dfs(node.right) # (True, 0)
            heightOfCurrNode = 1 + max(left[1], right[1])

            balanceCheck = left[0] and right[0]
            if not balanceCheck:
                return (balanceCheck, heightOfCurrNode)
            else:
                return (abs(left[1] - right[1]) <= 1, heightOfCurrNode)
        
        return dfs(root)[0]