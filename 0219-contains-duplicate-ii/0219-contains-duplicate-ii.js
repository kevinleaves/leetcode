/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
  var hash = {};
  //iterate thru nums
  for (var i = 0; i < nums.length; i++) {
    if (hash[nums[i]] === undefined) {
      hash[nums[i]] = i;
    } else {
      if (Math.abs(i - hash[nums[i]]) <= k) {
        return true
      } else {
        hash[nums[i]] = i;
      }
    }
  }
  //hash table store value + index
  //if i come across the value again, compare curr index to stored idx, if that passes condition, early return true
  // else continue with the loop
  return false
};