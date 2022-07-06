/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
  //initialize count variable
  var count = 0
  //iterate between low and high
  //if odd ++ to count
  
  for (low; low <= high; low++) {
    if (low % 2 === 1) {
      count++
    }
  }
  
  //return a count
  return count
};