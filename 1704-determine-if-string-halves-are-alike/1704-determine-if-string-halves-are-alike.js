/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
  var vowels = {
    a: 0,
    e: 0,
    i: 0,
    o: 0,
    u: 0,
  };
  //check if char is a vowel
  var isVowel = function (char) {
    return char in vowels || char.toLowerCase() in vowels
  }
  
  var count1 = 0;
  var count2 = 0;
  var l = 0
  var r = s.length - 1
  
  while (l < r) {
    if (isVowel(s[l++])) {
      count1++
    }
    if (isVowel(s[r--])) {
      count2++
    }
  }
  
  return count1 === count2
};