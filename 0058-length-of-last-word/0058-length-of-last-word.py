class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        find starting left idx
        start there, go left and store maximum
        '''
        s = ' ' + s + ' '
        
        r = len(s) - 1
        
        while s[r] == ' ':
            r -= 1
        
        l = r

        while l > 0 and s[l] != ' ':
            l -= 1
        
        return r - l