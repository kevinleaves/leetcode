class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        a string is a palindrome if it reads the same forwards and backwards
        can: reverse the string and strictly compare the two
        or:
        two pointers, one at the start and end
        while left is <= right
        increment left += 1
        decrement right -= 1
        only compare chars if they're not whitespace or special characters
        once pointers valid, compare the lowercase versions of both chars
        if they're not equal
          early return false
        
        
        o: return boolean. true if s is a palindrome, false if not
        '''
        left = 0
        right = len(s) - 1

        while left < right:
          if not s[right].isalnum():
            right -= 1
          
          if not s[left].isalnum():
            left += 1

          if s[left].isalnum() and s[right].isalnum():
            if s[left].lower() != s[right].lower():
              return False
            right -= 1
            left += 1
        
        return True

        

