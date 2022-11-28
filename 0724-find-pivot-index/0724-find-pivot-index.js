/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
  
  if (nums.length === 1) {
    return 0;
  }

  var sumLeft = [];
  var sumRight = [];

  //iterate through nums and update sumleft and sumright, compare values
  for (var i = 0; i < nums.length; i++) {
    
    var leftSum = sumLeft.reduce(function (acc, item) {
        return acc + item;
      }, 0)
    
    sumRight = nums.slice(i+1, nums.length);
    
    var rightSum = sumRight.reduce(function (acc, item) {
      return acc + item;
    }, 0)
    
  //if they're ever equal return i
    if (rightSum === leftSum) {
      return i;
    } 
    
    sumLeft.push(nums[i]);
  }
  
  return -1
};