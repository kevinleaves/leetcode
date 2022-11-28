/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
  // input array
  // output: array
  // constraints: nums always > 1, 
  // edgecases:
  // [sum(0,i=0), sum(0,i=1), sum(0,i=2), sum(0,i=3)]
  
  //in place: no extra memory needed
  // iterate through base array: for every number
  for (var i = 1; i < nums.length; i++) {
    //add element to sum
    nums[i] += nums[i - 1]; 
  }
  
  return nums;
};

