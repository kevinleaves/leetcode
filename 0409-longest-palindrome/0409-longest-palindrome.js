/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
  let set = new Set();
  let result = 0;
  for (let i = 0; i < s.length; i++) {
    if(set.has(s[i])) {
      result += 2
      set.delete(s[i])
    } else {
      set.add(s[i])
    }
  }
  return result + (set.size ? 1 : 0)
}
  
  