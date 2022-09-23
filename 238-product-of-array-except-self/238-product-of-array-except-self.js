/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    //2 iterations, once to establish prefixes, then iterate from the right, multiply by postfix product
    let prefixProduct = 1;
    let result = [];
    for (let i = 0; i < nums.length; i++) {
        result.push(prefixProduct)
        prefixProduct *= nums[i];    
    }
    
    let postfixProduct = 1;
    for (let i = nums.length-1; i >= 0; i--) {
        result[i] = postfixProduct * result[i]
        postfixProduct *= nums[i]
    }
    return result
};