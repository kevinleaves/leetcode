/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
  var count = 0
  //2 pointers i j
  for (var i = 0; i < nums.length; i++) {
      for (var j = i+1; j < nums.length; j++) {
          console.log('i: ', i, 'j: ', j)
          if (nums[i] === nums[j]) {
              count++
          }
      }
  }
  //j is always +1 i
  //compare numbers at i and j, if numbers the same count ++
    return count
};