/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  //create two pointers (high within the loop)
  //create max variable to hold max
  var max = 0
  var low = 0
  
  //iterate through array
  for (var high = 0; high < prices.length ; high++) {
    
    var difference = prices[high] - prices[low];
    //shift low pointer
    if (prices[high] < prices[low]) {
      low = high
    }
    
    // if (difference < 0) {
    //   low = high;
    // }
    
    //finding max
    if (difference > max) {
        max = difference;
    }
  }

  return max
};

