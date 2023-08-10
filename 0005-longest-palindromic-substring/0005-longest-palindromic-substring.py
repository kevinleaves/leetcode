class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        i: string s containing only digits & english letters
        o: string (the longest palindromic substring)
        c: none
        e: 

             
        babad

        store res
        update res with max length palindromic substring as we traverse
        2 pointers? 3 pointers?
        sliding window


        [x][aba][x]

        '''
        # returns if a string is a palindrome. save time by passing in indicies and not the actual substring
        def isPalindrome(i, j) -> bool:
            l, r = i, j - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        # check all substrings by length in decreasing order
        for length in range(len(s), 0, -1):
            # find valid start points for each possible substring length
            # a string length 4 for input "babad", means only possible start points are 0, 1. which means start should iterate from range 0 -> 2. infer how to calculate 2 using length 5. 5 - 4 + 1
            for start in range(0, len(s) - length + 1):
                if isPalindrome(start, start + length):
                    return s[start: start + length]

        return ''
