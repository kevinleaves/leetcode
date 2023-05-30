class Solution:
    def reverseVowels(self, s: str) -> str:
        s = [char for char in s]
        l, r = 0, len(s) - 1
        vowels = {"a", "e", "i", "o", "u"}
        while l < r:
            # ensure left is valid
            while s[l].lower() not in vowels and l < r:
                l += 1
            # ensure right is valid
            while s[r].lower() not in vowels and l < r:
                r -= 1
            # once valid spots, perform swap and move pointers
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)
