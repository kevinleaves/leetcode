class Solution:
    def isPalindrome(self, s: str) -> bool:
        #transform string into all lowercase
        #remove nonalphanumeric
        #reverse [::-1]
        
        
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())
        s2 = s[::-1]
        return s==s2