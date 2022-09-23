/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    //freq table from magazine
    let freq = {};
    for (let i = 0; i < magazine.length; i++) {
        freq[magazine[i]] = (freq[magazine[i]] || 0) + 1;
    }
    //iterate through ransomnote
    for (let i = 0; i < ransomNote.length; i++) {
        if (freq[ransomNote[i]] === 0) {
            return false
        }
        //if current letter exists in magazine
            //-1
        //if it doesn't
            //return false
        if (freq[ransomNote[i]]) {
            freq[ransomNote[i]]--
        } else {
            return false
        }
    }
    
    //return true if loop ends with no falses
    return true
        
        
    
};