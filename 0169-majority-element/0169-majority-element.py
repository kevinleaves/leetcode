class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        i: int array nums
        o: num within int that occurs more than n/2 times
        c: O(1) space, O(n) time follow up
        e: 
        '''
        
        '''
        solution 1:
        O(N) time, O(n) space
        count = collections.Counter()
        for num in nums:
          count[num] += 1
        
        return count.most_common(1)[0][0]
        '''

        # issue: how do i track occurences of a number as i iterate without using 
        # a hashmap/dict
        # can i use a single constant to track? 
        '''
        res = 0
        count = 0
        for num in nums:
          # the first number is always the majority at first
          if count == 0:
            res = num

          count += (1 if res == num else -1)
          # print(count)
        return res
        '''

        threshHold = math.ceil(len(nums) / 2)
        count = {}
        for num in nums:
          count[num] = count.get(num, 0) + 1
          if count[num] >= threshHold:
            return num
        

