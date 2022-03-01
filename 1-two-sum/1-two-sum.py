class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        #iterate through array
        #test for condition if target - value is in the hashmap
        #return indices of 2 numbers in res array
        for idx, value in enumerate(nums):
            if target - value in seen:
                return seen[target-value], idx
            else:
                seen[value] = idx
        
        
