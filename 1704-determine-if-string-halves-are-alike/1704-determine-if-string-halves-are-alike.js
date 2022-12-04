/**
 * @param {string} s
 * @return {boolean}
 */
var halvesAreAlike = function(s) {
  //fn to count vowels in a string: return the # of vowels
  var countVowels = function (s) {
    var vowels = 'aeiouAEIOU'
    var count = 0;
    for (var i = 0; i < s.length; i++) {      
      if (vowels.indexOf(s[i]) !== -1) {
        count++
      }
    }
    return count;
  }
  
  //run fn on both halves of the string
  return countVowels(s.substring(0, s.length/2)) === countVowels(s.substring(s.length/2, s.length))
};