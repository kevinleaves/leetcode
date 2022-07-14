/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  //create obj
  //iterate through array
  //short circuit?
  var seen = {};
  for (var i = 0; i < nums.length; i++) {
    var num = nums[i];
    if (num in seen) {
      return true
    }
    seen[num] = seen[num] + 1 || 1 
  }
  return false
};