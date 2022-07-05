/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    //create seen map
    //create result array
    var seen = {};
    var result = []; 
    
    //iterate through array
    for (var i = 0; i < nums.length; i++) {
      var currentNumber = nums[i];
      //if target - current number exists in seen as a key
      if (seen[target - currentNumber] !== undefined) {
        //push seen index and current index to result array
        result.push(i)
        result.push(seen[target - currentNumber])
      } else {
        // else store index and value inside seen map as value: index
        seen[currentNumber] = i
      }
    }
  
  //return result array
  return result
};