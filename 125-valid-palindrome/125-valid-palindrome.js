/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
  //remove all non-ascii chars
  //convert string to all lowercase

  s = s.toLowerCase();
  s = s.replace(/[^a-z0-9]/g, "");
  
  //return (comparison between reversed clean string and original cleaned string)
  return s.split("").reverse().join("") === s
};
