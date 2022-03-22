class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #rules of an anagram
        #all original letters used exactly once
        #rearranged letters
        #hashmap?
        hashMapS, hashMapT = {}, {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hashMapS[s[i]] = 1 + hashMapS.get(s[i], 0)
            hashMapT[t[i]] = 1 + hashMapT.get(t[i], 0)
            
        for c in hashMapS:
            if hashMapS[c] != hashMapT.get(c, 0):
                return False
            
        return True
            