/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    //current sum = first number
    let maxSum = nums[0]; //5
    //max sum = 0
    let currSum = 0; //0
    
    // if (nums.length === 1) {
    //     return currSum
    // }
    
    //iterate through nums
    for (let i = 0; i < nums.length; i++) {
        if (currSum < 0) {
            currSum = 0;
        }
        currSum += nums[i];
        maxSum = Math.max(currSum, maxSum)
    }
        //if current sum < 0, set it to 0
        //current sum += num at current idx
        //maxsum contains the max of currentsum and maxsum
        
    return maxSum
};