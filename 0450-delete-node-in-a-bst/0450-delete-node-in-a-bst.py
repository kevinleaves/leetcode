# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
        values in BST are unique
        key does not have to exist in BST => if it doesn't exist, we just return the original BST
        BST => binary search => logN
        BST => left node < parent, right node > parent

        for every node, check if it's equal to the key
        dfs or bfs

        1. If the target node has no child, we can simply remove the node.
        2. If the target node has one child, we can use its child to replace itself.
        3. If the target node has two children, replace the node with its in-order successor or     predecessor node and delete that node.

        '''

        # search for the node with key
        # identify # of children of that found node
            # if node has 0 children, delete by returning None
            # if node 1 child, swap

        def successor(node):
            curr = node
            curr = curr.right
            while curr.left:
                curr = curr.left
            return curr

        if not root:
            return None
        
        # find node to delete using BST properties
        if root.val > key:
            # search leftside
            left = self.deleteNode(root.left, key)
            root.left = left
        elif root.val < key:
            # search right side
            right = self.deleteNode(root.right, key)
            root.right = right
        else:
            # we've found our node to delete
            # if node only has 1 child, return the other subtree up to the parent
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # node has 2 children: find min from right subtree
            successorNode = successor(root)

            # change current node val to successor
            root.val = successorNode.val

            # delete duplicate node. 1 possible method of deletion is setting a nodes left/right to None
            root.right = self.deleteNode(root.right, successorNode.val)

        return root

            
