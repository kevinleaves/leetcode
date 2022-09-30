/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  let seen = {};
  //hashmap for seen values
  //iterate through nums array
  for (let i = 0; i < nums.length; i++) {
    if (target - nums[i] in seen) {
      return [seen[target - nums[i]], i] 
    } else {
      seen[nums[i]] = i  
    }
  }
    //if target - current number is in hashmap
      //return index value + current index
};