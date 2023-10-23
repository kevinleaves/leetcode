class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        create hashmap with this shape
        seen[num] = [num]

        init res to return later
        iterate through nums
        for each number:
            # populate seen[num] with consecutive numbers
            while num + 1 in seen:
                add array at num + 1 to current subarray
            update res to the max of current res and seen[num]

        return res
        '''
        if len(nums) == 0:
            return 0
            
        res = 1
        hash = set()
        for num in nums:
            hash.add(num)
        for num in nums:
            if num - 1 in hash:
                # we are not at the start of a sequence, continue
                continue
            else:
                # init new streak
                streak = 1
                start = num
                # we have a start of a sequence, find length of current streak
                while start + 1 in hash:
                    streak += 1
                    start += 1
                res = max(res, streak)
        return res

