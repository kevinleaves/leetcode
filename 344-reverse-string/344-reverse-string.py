class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #2 pointers
        #l, r
        #swap l,r, 
        #increment l, decrement r
        l, r = 0, len(s)-1
        while l < r:
            print(l, r)
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        