/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
  let l = 0;
  let r = nums.length-1;
  let sorted_idx = r;
  let sorted = [];
  
  while (sorted_idx > -1) {
    if (Math.abs(nums[r]) < Math.abs(nums[l])) {
      sorted[sorted_idx] = nums[l] ** 2
      l++
      sorted_idx--
    } else {
      sorted[sorted_idx] = nums[r] ** 2
      r--
      sorted_idx--
    }
  }  
  return sorted
};