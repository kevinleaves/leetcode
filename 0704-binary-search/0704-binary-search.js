/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

// [1, 2] target = 3
var search = function(nums, target) {
  //left, right pointers
  var l = 0;
  var r = nums.length - 1;
  
  //while condition
  while (l <= r) {
    var mid = Math.floor(l + (r - l)/2)
    if (nums[mid] === target) {
      return mid
    } else if (nums[mid] > target) {
      r = mid - 1;
    } else {
      l = mid + 1;
    }
  }
  
    //find midpoint
    //if num at midpoint === target: return midpoint
    //if num at midpoint > target: chop off rightside
    //if num at midpoint < target: chop off leftside
  
  //return -1 if loop exits and not found
  return -1
};