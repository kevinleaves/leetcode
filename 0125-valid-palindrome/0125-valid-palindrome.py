class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        '''
        establish 2 pointers, left and right. starting at the edges of the string
        while l <= r
            move l pointer until valid character (skip all spaces)
            while s[l] isn't alnum
                increment l

            move r pointer until valid character (skip all spaces)
            while s[r] isn't alnum
                decrement r

            once valid characters
            compare them
            if they're not the same
                return false
            
        loop finishes without returning false, return true
        '''
        l, r = 0, len(s) - 1
        while l <= r:
            while l <= r and not s[l].isalnum():
                l += 1
            while l <= r and not s[r].isalnum():
                r -= 1
            if l <= r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

