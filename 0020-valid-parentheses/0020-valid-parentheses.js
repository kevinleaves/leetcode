/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  let hash = {')': '(', '}': '{', ']': '['}
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    if (char === '(' || char === '{' || char === '[') {
      stack.push(char)
    } else {
      if (stack[stack.length-1] === hash[char]) {
        stack.pop()
      } else {
        return false
      }
    }
  }
  return stack.length === 0
};