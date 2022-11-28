/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
// init len
  var len = 0;
// get last index of s
  var lastIndex = s.length - 1;

// find true last character of the last word
  while (lastIndex >= 0 && s[lastIndex] === ' ') {
    lastIndex--
  }

//   now we're at the last char truly
  while (lastIndex >= 0 && s[lastIndex] !== ' ') {
    len++
    lastIndex--
  }  
  
  //return length
  return len
};