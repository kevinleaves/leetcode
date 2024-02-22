class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixes = self.generatePrefixes(nums)

    def generatePrefixes(self, nums: List[int]):
      prefixes = [0]*len(nums)
      prefixSum = 0
      for i in range(len(prefixes)):
        prefixSum += nums[i]
        prefixes[i] = prefixSum
      return prefixes
      

    def sumRange(self, left: int, right: int) -> int:
      # naive way, inefficient recalulcate every time sumRange gets called
      # trade space for time, can calculate range using prefixes array
      rightSum = self.prefixes[right]
      leftSum = self.prefixes[left - 1] if left > 0 else 0 
      return rightSum - leftSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)