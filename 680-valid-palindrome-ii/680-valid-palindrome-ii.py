class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        deletes = 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r] and deletes == 0:
                return False
            elif s[l] != s[r] and deletes == 1:
                # check both possibilities if palindrome
                deletes -= 1
                if self.isPalindrome(s[:l] + s[l + 1 :]) or self.isPalindrome(
                    s[:r] + s[r + 1 :]
                ):
                    return True
        return True

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
