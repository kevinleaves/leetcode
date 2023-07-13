# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        print(nums)
        '''
        i: nums array sorted asc
        o: height balanced bst
        c: none
        e: none
        To convert a sorted array to a binary search tree, we can use the following recursive algorithm:

If the array is empty, return null.
Find the middle element of the array and create a new node with its value.
Recursively construct the left subtree using the left half of the array.
Recursively construct the right subtree using the right half of the array.
Set the left and right child of the node created in step 2 to the root of the left and right subtree respectively.
Return the root node.

        '''
        if not nums:
            return None
        
        l, r = 0, len(nums) - 1
        mid = l + r // 2
        midNode = TreeNode(nums[mid])
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid+1:])

        # attach nodes to mid
        midNode.left = left
        midNode.right = right
        return midNode

