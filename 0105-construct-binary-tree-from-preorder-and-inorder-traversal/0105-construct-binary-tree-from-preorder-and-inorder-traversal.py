# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''

        i: 2 int arrays
        o: root node of constructed btree using array nodes
        c: none
        e: 
        
        preorder = [3,9,20,15,7]

        inorder = [9,3,15,20,7]
        '''
        # build root
        if not preorder:
            return None

        if not inorder:
            return None

        root = TreeNode(preorder[0])

        rootIdx = inorder.index(preorder[0]) 
        leftTree = inorder[:rootIdx]
        rightTree = inorder[rootIdx + 1:]

        szleft = len(leftTree)
        szright = len(rightTree)
        
        preorderLeft = preorder[1: 1 + szleft]
        preorderRight = preorder[1 + szleft:]
        
        # buildTree takes in 2 arrays
        left = self.buildTree(preorderLeft, leftTree)
        root.left = left
        # buildTree takes in 2 arrays
        right = self.buildTree(preorderRight, rightTree)
        root.right = right
        
        # return root
        return root
        