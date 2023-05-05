# non cs way


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c
        cleaned = cleaned.lower()
        return cleaned == cleaned[::-1]


# 48.52, 17.20%
