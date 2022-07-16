/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
  var result = []
  var counter = {};
  for (var num of nums1) {
    counter[num] = counter[num] + 1 || 1
  }
  
  for (var j of nums2) {
    if (counter[j] > 0) {
      result.push(j)  
      counter[j]--
    }
  }
  console.log(counter)
  return result
};