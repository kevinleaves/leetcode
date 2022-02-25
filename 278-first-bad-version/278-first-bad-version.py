# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        #while exits when l >= r
        while l < r:
            mid = l + (r - l) //2
            if isBadVersion(mid):
                r = mid
            else: #not isBadVersion(mid):
                l = mid+1
        return r            
 
                
        
        #if isBadVersion(mid-1):
         #           return mid-1