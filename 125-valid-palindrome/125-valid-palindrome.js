/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    function isASCII (char) {
        let pattern = /\w/g;
        return pattern.test(char)
    }
    
    //left and right pointers
    //check if char at left and right are ===
    //if they aren't return false
    //if they are, left += 1, right -= 1
    //if char is nonascii go next char
    //loop breaks when l > r
    
    s = s.toLowerCase().replace(/[^a-z0-9]/g, '')
                       
    for (let i = 0, j = s.length-1; i <= j; i++, j--) {
        if (s[i] !== s[j]) {
            return false
        }
    }
    
    return true
};