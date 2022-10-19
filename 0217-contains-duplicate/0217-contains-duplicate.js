/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    //create a set
    let set = new Set()
    
    //iterate through array
    for (let i = 0; i < nums.length; i++) {
      if (set.has(nums[i])) { 
        return true //if num is in set, return true
      } else { 
        set.add(nums[i]) //if num isnt in set, add num to set
      }
    }
  
    return false //return false once loop ends with no trues
} 