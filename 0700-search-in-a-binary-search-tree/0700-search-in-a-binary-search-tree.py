# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        i: root of bst, val int to search for
        o: node with the target val. return that node/subtree
        c: none
        e: node does not exist within the bst, return null

        bst properties mean we only need to search 1/2 of the subtree based on the val

        establish curr pointer at root
        if val < node.val:
          traverse left (move pter)
        else if val > node.val:
          traverse right (move pter)
        else:
          # val === node.val
          return node

        '''

        curr = root
        while curr:
          if val == curr.val:
            return curr
          elif val > curr.val:
            curr = curr.right
          else:
            curr = curr.left
        
        # if we don't return anything and we reach the end of the traversal return null
        return None

