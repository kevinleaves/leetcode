class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        i: string
        o: int
        c: none
        e: eeeeeeeee => 1. length 0 s => 

        max = 1
        l
        pwwkew
         r
        
        freq table that stores char: frequency of char in current window
        variable to store max, we update this as we slide
        start 2 pointers at beginning, pointers represent window
        increment right pointers
        check if window is valid
            if valid, we update max to be our current window length
            if not valid, slide left pointer to left until the window is valid again, remove character from freq

        {a4 b2 c3 
        }
        '''

        freq = {}
        res = 0
        l, r = 0, 0
        
        while l <= r and l < len(s) and r < len(s):
            curr = s[r]
            freq[curr] = freq.get(curr, 0) + 1
            # check for invalid
            if freq[curr] > 1:
                # remove char at left until valid
                while freq[s[r]] > 1:
                    freq[s[l]] -= 1
                    l += 1
            
            res = max(res, r - l + 1)    
            r += 1

        return res

