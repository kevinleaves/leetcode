/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum = 0;
    int maxDepth = 0;
    public int deepestLeavesSum(TreeNode root) {
    // how do i determine tree traversal order?  
    // find max depth
    // find sum of all nodes at that depth
      findMaxDepth(root, 0);
      findSum(root, 0);
      return sum;
    }

    public int findMaxDepth(TreeNode node, int depth) {
      // postorder
      if (node == null) {
        return -1;
      }

      // recursive step
      findMaxDepth(node.left, depth + 1);
      findMaxDepth(node.right, depth + 1);
      maxDepth = Math.max(maxDepth, depth);
      return 0;
    }

    public int findSum(TreeNode node, int depth) {
      if (node == null) {
        return -1;
      }

      findSum(node.left, depth + 1);
      findSum(node.right, depth + 1);
      if (depth == maxDepth) {
        sum += node.val;
      }
      return 0;
    }

}