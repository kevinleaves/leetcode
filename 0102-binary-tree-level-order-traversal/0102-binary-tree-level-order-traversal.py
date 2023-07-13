# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        i: root of btree
        o: array of subarrays, each subarray contains all nodes at ith level
        c: none
        e: root empty => return empty
        '''

        res = []
        q = collections.deque()

        if root:
            q.appendleft(root)
        
        # how do we know that we've cleared a level
        # answer: use a for loop to process an entire level's nodes. we still pop nodes 1 at a time, but this allows us to populate a subarray
        while q:
            # process nodes 1 level a time
            level = []
            for i in range(len(q)):
                node = q.popleft()
                # add an entire level's children to the q.
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # subarray stuff
                level.append(node.val)
            res.append(level)
        return res

        