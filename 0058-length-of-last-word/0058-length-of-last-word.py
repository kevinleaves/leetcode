class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        iterate from right to left
        point to valid right
        decrement left until it reaches a whitespace

        return window size
        '''
        right = len(s) - 1
        while right >= 0 and not s[right].isalnum():
          right -= 1

        left = right
        while left >= 0 and s[left].isalnum():
          left -= 1
        # left should be at a whitespace character
        return right - left