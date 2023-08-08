class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        i: 2 strings, needle and haystack consisting of lowercase english letters
        o: index of first occurrence of needle in haystack
        c: none
        e: if not found, return -1
        
              l r
        aadbutsad
        
        sad

        instantiate window from left to right, window is always size of len needle
        l - r + 1 == window size
        if haystack[slice] == needle, return l index
        otherwise increment both left and right by 1
        stop loop when r reaches end of haystack
        '''

        if len(needle) > len(haystack):
            return -1
        
        l, r = 0, len(needle) - 1
        while l <= r and r <= len(haystack) - 1:
            if haystack[l : r + 1] == needle:
                return l
            l += 1
            r += 1

        return -1

        