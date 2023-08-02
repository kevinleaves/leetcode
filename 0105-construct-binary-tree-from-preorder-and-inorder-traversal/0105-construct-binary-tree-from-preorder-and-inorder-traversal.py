# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        preorder[0] gives us the root node [3]
        find 3 within inorder array, its left subarray is left tree, right subarray is right tree
        preorder is node, left, right, use inorder subarray lengths to split preorder array
        recursively build tree by passing in new preorder and inorder arrays to buildtree

        '''
        if not preorder or not inorder:
            return None

        root = preorder[0]
        pivot = inorder.index(root)
        inorderLeft = inorder[:pivot]
        inorderRight = inorder[pivot+1:]
        preorderLeft = preorder[1:1+len(inorderLeft)]
        preorderRight = preorder[1+len(inorderLeft):]
        
        left = self.buildTree(preorderLeft, inorderLeft)
        right = self.buildTree(preorderRight, inorderRight)

        res = TreeNode(root)
        res.left = left
        res.right = right
        
        return res
        

