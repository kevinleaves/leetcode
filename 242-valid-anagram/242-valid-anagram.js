/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  //writing out 2 false conditions, if none of them hit false, return true
  //automatically false if two strings are different length
  if (s.length !== t.length) {
    return false
  }
  //popular counts dictionary with counts of all characters
  const counts = {};
  for (let char of s) {
    if (!(char in counts)) {
      counts[char] = 1  
    } else {
      counts[char] += 1
    }
  }
  
  console.log(counts)
  //iterate through second string, 
  for (let c of t) {
    if (!counts[c]) {
      return false
    }
    counts[c]--;
  }
  console.log(counts)
  //if no false conditions are satisfied, return true
  return true
};
