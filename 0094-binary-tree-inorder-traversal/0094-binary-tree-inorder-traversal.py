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
        
        # use a pointer to traverse in iterative solution
        curr = root    
        # consider this loop the equivalent of a recursive call
        while stack or curr:
            # this while loop is essentially a base case
            # go left as much as we can
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # curr has reached all the way to the left/curr is null, we can perform actions now
            # top of the stack is our leftmost node

            # a stack pop is basically a recursion return. every time we hit a null we pop
            curr = stack.pop()
            # inorder traversal
            res.append(curr.val)
            curr = curr.right
            
        return res

