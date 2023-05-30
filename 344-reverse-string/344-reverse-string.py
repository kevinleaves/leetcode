class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # pointers l, r
        l, r = 0, len(s) - 1
        while l < r:
            # swap chars at l & r
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            # l++, r--
            l += 1
            r -= 1

        return s
