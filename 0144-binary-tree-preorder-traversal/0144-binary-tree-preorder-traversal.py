# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # node, left, right
        # process first, explore left nodes, explore right nodes.
        # iterative => emulate recursion using a stack + pointer

        res = []
        curr = root
        stack = []

        '''
        [1 2 4 5 6]
        res = [1 2 4]
        stack =[3 5]
         1
        2 3
       4 5
          6

        where i went wrong? i was missing the condition of when curr == None. didn't identify that i either move left OR i pop to return right. we're also able to add null nodes here because we take care of that scenario in our base case
        '''
        while stack or curr:
            # when do we pop? when we're done going left. notice we have no while loops here
            if not curr:
                curr = stack.pop()
            else:
                # process node
                res.append(curr.val)
                
                # add right node so we can pop back to right
                stack.append(curr.right)

                # go left. if curr == none that's base case, then we pop and go right
                curr = curr.left

        return res
