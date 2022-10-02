/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    //make hashstr for s
    let hashS = new Array(26).fill(0)
    for (let char of s) {
      hashS[char.charCodeAt(0) - 'a'.charCodeAt(0)]++
    }
    
    //make hashstr for t
    let hashT = new Array(26).fill(0)  
    for (let char of t) {
      hashT[char.charCodeAt(0) - 'a'.charCodeAt(0)]++
    }
  
    //compare 2 hashstrs
    return hashS.toString() === hashT.toString()
};