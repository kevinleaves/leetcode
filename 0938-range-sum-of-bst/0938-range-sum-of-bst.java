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
    public int rangeSumBST(TreeNode root, int low, int high) {
        // base case
        if (root == null) {
          return 0;
        }

        // additional base cases utilizing BST properties
        if (root.val < low) {
          return rangeSumBST(root.right,low, high);
        }
        if (root.val > high) {
          return rangeSumBST(root.left,low, high);
        }

        int sum = 0;
        
        // if node val is within range, include it in the sum
        if (root.val >= low && root.val <= high) {
          sum += root.val;
        }
    
        sum += rangeSumBST(root.left, low, high);
        sum += rangeSumBST(root.right, low, high);

        return sum;
    }
}