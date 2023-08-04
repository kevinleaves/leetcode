"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        make every node's next pointer point to the node to its right
        if that doesn't exist, make it point to null
        q = []
        len(q) == 4


        bfs (level order traversal)
        make every node point to the node at the current top of the q
        if we're at the last element in the level, make that node point to null
        '''
        
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            level = len(q)
            for i in range(level):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                # treat level as if it were a linked list. if we're at the last node, make it point to null instead of q[0]
                if i == level - 1:
                    node.next = None
                else:
                    node.next = q[0]

        return root
