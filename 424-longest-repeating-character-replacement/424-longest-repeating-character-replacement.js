/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
  //create counter hashmap
  let counter = {}
  //left and right pointers
  let l = 0;
  //maxLength
  let maxLength = 0;
  //iterate through string
  for (let r = 0; r < s.length; r++) {
    // console.log(s[r])
    counter[s[r]] = (counter[s[r]] || 0 ) + 1
    let values = Object.values(counter)
    let max = Math.max(...values)
    let algo = (r - l + 1) - max 
    // console.log('algo: ', algo)
    if (algo <= k) {
      maxLength = r - l + 1
    } else {
      counter[s[l]]--
      l++
    } 
  }
  return maxLength
    //populate counter with current letter
  //length of window - length of largest counter <= k
  //if it isn't, shift l += 1, decrement that counter
  
};