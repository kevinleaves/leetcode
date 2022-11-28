/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  // create set
  var set = new Set();
  // iterate through nums
  for (var i = 0; i < nums.length; i++) {
    if (set.has(nums[i])) {
        return true
    } else {
      set.add(nums[i])
    }
  }
//   if element in set, return true
//   if element doesnt exist in set, add it to set
  
//   if iteration finishes completely return false
  return false
};