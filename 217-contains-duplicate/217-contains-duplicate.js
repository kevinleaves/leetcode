/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    //create duplicate array
    let copy = [];
    //create boolean flag = false
    let duplicate = false;
    
    //iterate through original array
    for (let i = 0; i < nums.length; i++) {
        if (copy.indexOf(nums[i]) === -1) {
            copy.push(nums[i])
        } else {
            duplicate = true;
        }
    }
        //if element isn't in duplicate array
            //push it to duplicate
        //else
            //flip boolean flag to true
    //return boolean
    return duplicate
};