/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    //populate results array with prefixes 
    //iterate from right, track suffixes and multiply each prefix element by its suffix to get result
    let res = [];
    let prefix = 1;
    
    for (let i = 0; i < nums.length; i++) {
        res[i] = prefix;      
        prefix *= nums[i];
    }
    
    let postfix = 1;
    for (let j = nums.length-1; j>=0; j--) {
        res[j] *= postfix
        postfix *= nums[j];
    }

    return res
};