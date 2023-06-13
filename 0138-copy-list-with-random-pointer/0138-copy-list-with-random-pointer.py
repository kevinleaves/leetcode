"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # edgecase: n = 0
        if not head:
            return None
        # 2 passes. first pass creates deep copies of the nodes & creates hashmap mapping oldNode -> newNode
        # 2nd pass -> create links

        nodeMap = dict()
        curr = head
        while curr:
            clone = Node(curr.val)
            nodeMap[curr] = clone
            curr = curr.next
        # now we have a reference to every clone node
        # iterate through original head again, set clone pointers
        curr = head
        newHead = nodeMap[curr]
        while curr:
            clone = nodeMap[curr]
            clone.next = nodeMap.get(curr.next)
            clone.random = nodeMap.get(curr.random)
            curr = curr.next
        
        return newHead
         
        

        