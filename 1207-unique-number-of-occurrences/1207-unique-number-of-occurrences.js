/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
  var freq = {};
  arr.forEach(function(item) {
    freq[item] = (freq[item] || 0) + 1;
  })
  
  var freq2 = {}
  Object.values(freq).forEach(function (item) {
    freq2[item] = (freq2[item] || 0) + 1; 
  })
  
  return Object.values(freq2).every(function (item) {
    return item === 1
  })
};