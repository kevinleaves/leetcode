class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        i:
        o: bool. true if s is a subsequence of t
        subsequence: if i can remove chars from t and get s by maintaining order
        
        {a1 b2 c1}
            p
        s = abbc
        t = ahbbgdc
        [abbc] 
        => true

        s = abbc
        t = ahbgdcb -> false
        [abcb]

        s = z
        t = z

        s= ''
        t = ''
        '''
        if not s:
            return True

        p1 = 0
        p2 = 0

        while p2 < len(t) and p1 < len(s):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1

        return p1 >= len(s)