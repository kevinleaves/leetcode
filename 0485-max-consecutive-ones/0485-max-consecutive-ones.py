class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        i: binary array
        o: int (max num of consec 1s)
        c: none
        e: none
        
         
        [0,1,0,1,1,1]
        '''
        res = 0
        
        # 2 pointer
        # find valid L position, increment res by 1 once found

        l = 0
        while l < len(nums) and nums[l] == 0:
            l += 1

        # establish r pointer
        r = l
        while r < len(nums):
            # contract window
            if nums[r] == 0:
                while r < len(nums) and nums[r] == 0:
                    r += 1
                l = r

            # once we have a valid window, update res
            res = max(res, r - l + 1)
            r += 1
        
        return res