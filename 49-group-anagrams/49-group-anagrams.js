/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
  let mapping = {};
  for (let str of strs) {
    //create freq table/hashtable for each string
    let hash = new Array(26).fill(0)
    for (let i = 0; i < str.length; i++) {
      hash[str[i].charCodeAt(0) - 'a'.charCodeAt(0)]++  
    }
    
    //add hashstrings as mapping keys to store matching strings
    if (!mapping[hash]) {
      mapping[hash] = [];
    }
    
    //push the matching strings to the value array
    mapping[hash].push(str)
    
  }
  
  //this obj returns a nested array of obj values
  return Object.values(mapping)  
};

