/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
  
  //base case
  if (root === null) {
    return root
  }
  
  // var temp = root.left
  // root.left = root.right
  // root.right = temp
  
  //swap
  [root.left, root.right] = [root.right, root.left]
  
  //recursively call invertTree on left & right nodes
  invertTree(root.left)
  invertTree(root.right)
  
  return root
};