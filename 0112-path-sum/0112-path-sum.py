# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        i: root, target int
        o: boolean representing whether the tree contains a root to leaf path whos vals sum==target
        c: none
        e: empty tree => false

        only do target comparison if we've arrived at a leaf node
        '''
        if not root:
            return False

        def dfs(node, currPathSum):
            # base case(s)
            if not node:
                return (False, 0)
            
            currPathSum += node.val
            
            # recursive case(s)
            left = dfs(node.left, currPathSum)
            right = dfs(node.right, currPathSum)

            # only if leaf node
            isLeafNode = not left[0] and not right[0] and left[1] == 0 and right[1] == 0
            if isLeafNode and currPathSum == targetSum:
                return (True, currPathSum)
            else:
                return (left[0] or right[0], currPathSum)
        return dfs(root, 0)[0]



        