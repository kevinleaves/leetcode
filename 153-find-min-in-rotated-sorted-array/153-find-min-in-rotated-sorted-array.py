class Solution:
    def findMin(self, nums: List[int]) -> int:
        minElement = float(inf)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                minElement = min(minElement, nums[mid])
                r = mid - 1
            else:
                l = mid + 1
        return minElement
