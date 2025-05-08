class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            # compute current sum
            current_sum = nums[l] + nums[r]
            
            if current_sum < target: # shift left pointer up to increase the total
                l += 1
            elif current_sum > target: # shift right pointer down to decrease the total
                r -= 1
            else:
                return [l + 1, r + 1]
