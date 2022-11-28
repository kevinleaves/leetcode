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
  
  var sum = 0;
  var res = [];
  
  // iterate through base array: for every number
  for (var i = 0; i < nums.length; i++) {
    //add element to sum
    sum += nums[i]
    //push sum to res
    res.push(sum);
  }
  
  return res
};

