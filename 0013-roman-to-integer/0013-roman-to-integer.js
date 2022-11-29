/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
  //map to store symbol + value pairs
  var symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'CM': 900,
    'CD': 400,
    'XC': 90,
    'XL': 40,
    'IX': 9,
    'IV': 4
  };
  
  //store sum
  var total = 0;
  
  var i = 0;
  
  while (i < s.length) {
    //2 character substring
    if (i < s.length - 1 && s.substring(i, i+2) in symbols) {
      total += symbols[s.substring(i, i+2)]
      i+=2
    } else {
      total += symbols[s[i]]
      i++  
    } 
  }
    //if we run into certain chars, check next index for special chars
  
    
    //normal case
  
    //if we find special chars add them to sum
    //skip 2 indices
  return total
};