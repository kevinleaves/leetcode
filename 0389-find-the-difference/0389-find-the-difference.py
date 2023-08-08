class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''
        i: 2 strings s & t
        o: string the letter that's the difference
        c: none 
        e: 
        
        s gets shuffled
        t is s shuffled + 1 letter
        what if the +1 letter is one of the letters already in s

        s {a1 b1 c1 d2}
        t {a}
        look up key in s if it doesn't exist, return key
        if it exists in t, increment it by 1
            if number after increment is > s[key], return key
        if it exists in s, add it to t, set it to 1

        '''
        freqS = {}
        for char in s:
            freqS[char] = freqS.get(char, 0) + 1
        # print(freqS)
        freqT = {}
        for key in t:
            if key not in freqS:
                return key
            if key in freqT:
                freqT[key] += 1
                # print(freqT)
                if freqT[key] > freqS[key]:
                    return key
            else:
                freqT[key] = 1
        
                