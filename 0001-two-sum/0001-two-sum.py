class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        i: int[] 
        o: int[] representing indicies of numbers that add up to target
        c: 
        e:
        
        outer loop iterating (i) over nums.
            inner loop starting at i + 1, iterating until the end
                if outer num + inner num == target:
                    return [outernum, innernum]
        
        '''
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        
