/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  //automatically false if two strings are different length
  if (s.length !== t.length) {
    return false
  }
  //turn s and t into arrays
  arr1 = s.split('')
  arr2 = t.split('')
  //sort them
  return arr1.sort().join('') === arr2.sort().join('')
  //if they're equal, return true
  //else false
  
  
  
//return boolean
};
