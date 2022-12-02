/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var closeStrings = function(word1, word2) {
    //freq table for both words
    //if freq table same total length and same # of keys, then true
    //else false
  
    var freq1 = {};
    var freq2 = {};
    
    if (word1.length !== word2.length) {
      return false;
    };
  
    for (var i = 0; i < word1.length; i++) {
      freq1[word1[i]] = (freq1[word1[i]] || 0) + 1
    }
  
    for (var i = 0; i < word2.length; i++) {
        freq2[word2[i]] = (freq2[word2[i]] || 0) + 1
    }   
  

    // console.log(JSON.stringify(Object.values(freq1).sort(function (a, b) {
    //   return a-b;
    // })))
    var wordsArraySame = JSON.stringify(Object.values(freq1).sort(function (a, b) {
      return a-b;
    })) === JSON.stringify(Object.values(freq2).sort(function (a, b) {
      return a-b;
    }))
    
    var keysSame = JSON.stringify(Object.keys(freq1).sort()) === JSON.stringify(Object.keys(freq2).sort())
    
    return (Object.keys(freq1).length === Object.keys(freq2).length) && wordsArraySame && keysSame
};