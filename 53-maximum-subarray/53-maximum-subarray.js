/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
  //l, r pointers
  var result = nums[0]
  var l = 0
  var currSum = 0
      
  for (var r = 0; r < nums.length; r++) {
    if (currSum < 0) {
      l = r
      currSum = 0
    }
    currSum += nums[r]
    result = Math.max(currSum, result)
  }
  
  return result
};


