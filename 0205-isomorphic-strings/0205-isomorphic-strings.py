class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}
        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            # check if prior mappings already exist in both maps
            if c1 in mapST and mapST[c1] != c2:
                return False
            if c2 in mapTS and mapTS[c2] != c1:
                return False

            mapST[c1] = c2
            mapTS[c2] = c1                
        
        return True

