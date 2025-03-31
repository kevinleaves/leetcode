class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      '''
      there will always be a solution
      i: int[], unsorted
      o: return indices of the numbers that add up to the target
      c: no constraints, or less than n^2
      e: 
      '''

      hashmap = {}

      # if target - current number is not in hashmap as key: store the pair as value, index
      # else, return hashmap[value], current index

      for i, v in enumerate(nums):
        diff = target - nums[i]
        if diff in hashmap:
          return [hashmap.get(diff), i]
        else:
          hashmap[v] = i
      



            
        