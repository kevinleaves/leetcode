class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
      '''
      init 2 pointers,
      one starting at 0
      one starting at 0+n
      iterate from 0 to n
      
      O(N) time
      O(N) space
      '''
      res = [0]*len(nums)
      left = 0
      right = 0+n
      for i in range(0, 2*n, 2):
        res[i] = nums[left]
        res[i+1] = nums[right]
        left += 1
        right += 1
      return res

        