# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # base case for empty nums
        if not nums:
          return None
          
        idxOfMaxNum = nums.index(max(nums))
        left = nums[:idxOfMaxNum]
        right = nums[idxOfMaxNum + 1:]

        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)

        return root