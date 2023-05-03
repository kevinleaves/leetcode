class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # i: 2 strings, s & p
        # o: array of integers. ints representing start indices of P's anagrams in S
        # c: none
        # e: if s has no anagrams of p: return empty array. if len s < len p => return []
        if len(s) < len(p):
            return []

        res = []

        # make freq table for string p
        freqP = {}
        for c in p:
            freqP[c] = freqP.get(c, 0) + 1

        l = 0

        # right pointer loops through s indices
        window = {}
        for r in range(len(s)):
            # add current char to window
            window[s[r]] = window.get(s[r], 0) + 1

            # confirm valid window first
            while r - l + 1 > len(p):
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            # once confirmed valid, then check
            if r - l + 1 == len(p):
                if window == freqP:
                    res.append(l)

        return res


# 48.56% 5.12%
