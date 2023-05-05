class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # ensure l valid
            while not s[l].isalnum() and l < r:
                l += 1

            # ensure r valid
            while not s[r].isalnum() and l < r:
                r -= 1

            # compare chars at both ends
            if s[l].lower() != s[r].lower():
                return False

            # move pointers inward
            l += 1
            r -= 1

        return True


# 21.11% 17.20%
