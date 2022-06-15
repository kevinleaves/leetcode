/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    //create seen obj
    var seen = {}
    //create res array
    var res = []
    
    //iterate through nums
    for (var i = 0; i < nums.length; i++) {
      var currentNumber = nums[i];
      if (seen[target - currentNumber] !== undefined) {
        res.push(i);
        res.push(seen[target-currentNumber])
      } else {
        seen[currentNumber] = i  
      }
    }
      //if target - current number is in seen
         //res.push index of current number
         //res.push index of target - currentNumber
      //else
         //add current number to seen with its index as its value
    
    
    //return res array
    return res
};