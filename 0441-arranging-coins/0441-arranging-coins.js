/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function(n) {
  //input: number of coins
  // output: number of complete rows (number)
  // c: n > 1
  // e: 
  
  //l, r
  var left = 1;
  var right = n;
  
  //while condition
  while (left <= right) {
    // calc midpoint 1 -> n inclusive
    var mid = Math.floor(left + (right - left) / 2);
    // calc target (which is the number of coins needed to finish a row) remember formula n(n+1)/2
    var coinsNeeded = mid * (mid + 1) / 2; 
    // if midpoint === target, return mid
    if (n === coinsNeeded) {
      return mid;
    // if midpoint > target chop of right side
    } else if (n < coinsNeeded) {
      right = mid - 1;
    // if midpoint < target chop off left side
    } else {
      left = mid + 1;
    }
  }
  return right
};