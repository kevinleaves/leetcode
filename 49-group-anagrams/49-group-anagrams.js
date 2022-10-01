/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
  let mapping = {};
  for (let str of strs) {
    let hash = new Array(26).fill(0)
    for (let i = 0; i < str.length; i++) {
      hash[str[i].charCodeAt(0) - 'a'.charCodeAt(0)]++  
    }
      if (!mapping[hash]) {
      mapping[hash] = [];
    }
    mapping[hash].push(str)   
  }
  return Object.values(mapping)  
};

