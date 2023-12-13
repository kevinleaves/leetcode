function search(nums: number[], target: number): number {
    /**
    I: sorted num[], target number
    O: return index of target number if it exists in nums
    C: o(log n) time
    E: return -1 if target isn't in nums. nums array length 2

    STEPS:
    left, right variables
    calculate mid index
    if target === nums[mid] return mid
    if target is > nums[mid] chop off left -> left = mid + 1
    else target is < nums[mid] chop off right -> right = mid - 1
    
    while loop ends without returning a midpoint -> return -1

    while loop: while left is <= right (continues when left === right)
    */
    let l = 0
    let r = nums.length - 1 

    while (l <= r) {
        let mid = Math.floor((l + r) / 2)
        if (nums[mid] === target) {
            return mid
        } else if (nums[mid] < target) {
            l = mid + 1
        } else {
            r = mid - 1
        }
    }
    
    return -1
};