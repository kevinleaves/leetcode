/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
  let count = {}
  let majority = 0;
  let highestCount = 0;
  for (let i = 0; i < nums.length; i++) {
    count[nums[i]] = count[nums[i]] + 1 || 1
    if (count[nums[i]] > highestCount) {
      highestCount = count[nums[i]]
      majority = nums[i]
    }
  }
  return majority
};