/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
  // input array
  // output number
  //c: array never empty
  //e: if nums is 1 return that number
  if (nums.length === 1) {
    return nums[0];
  }
  
  // make obj
  var res = {};
  // add ele to obj if it isn't in obj
  for (var i = 0; i < nums.length; i++) {
    if (nums[i] in res) {
  // if ele is in obj, pop it out
      delete res[nums[i]]
    } else {
      res[nums[i]] = 1;
    }
  }
  // there should only be 1 remaining element at the end, get that element
  return Object.keys(res)[0];
};