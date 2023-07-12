# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        i: root and subRoot
        o: boolean representing whether root has a subtree with the exact same structure and node values of subRoot. true if it does, false if it does not
        c: 
        e: subroot will always be at least 1 node
        '''
        def sameTree(node1, node2):
            # base case(s)
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            equalVals = node1.val == node2.val    
            left = sameTree(node1.left, node2.left)
            right = sameTree(node1.right, node2.right)

            # recursive case(s)
            # if root has equal vals, check left + r subtree
            return equalVals and left and right

        if not subRoot:
            return True
        if not root:
            return False
        if sameTree(root, subRoot):
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right 
         

      

        
    
        

