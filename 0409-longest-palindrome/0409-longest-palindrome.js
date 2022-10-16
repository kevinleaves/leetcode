/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
  let hash = {};
  let result = 0;
  for (let i = 0; i < s.length; i++) {
    hash[s[i]] = hash[s[i]] + 1 || 1
    if (hash[s[i]] % 2 === 0) {
      result += 2
    }
  }
  
  if (result === s.length) {
    return result
  } else if (result < s.length)
    return result + 1
};