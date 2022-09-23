/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    //create freq table for string s
    //iterate through string t, for each char -1 char from freq table. if char doesn't exist return false if it does -1
    
    
    //if freq table is empty at the end return true
    let freq = {};
    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        freq[char] = freq[char] + 1 || 1;
    }
    
    for (let j = 0; j < t.length; j++) {
        let char = t[j];
        if (char in freq) {
            freq[char] = freq[char] - 1
        } else {
            return false
        }
    }        
    
    const isEmpty = Object.values(freq).every(x => x === 0)
    
    return isEmpty
};