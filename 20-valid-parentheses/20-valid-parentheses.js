/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(string) {
  var brackets = {"(" : ")", "{" : "}", "[" : "]"}
  var stack = [];
  
  for (char of string) {
    //if char is open bracket, push it to the stack,
    if (brackets[char] !== undefined) {
      stack.push(char)
    } else if (brackets[stack.pop()] !== char) {
      return false
    }
  } 
  
  return !stack.length
};
