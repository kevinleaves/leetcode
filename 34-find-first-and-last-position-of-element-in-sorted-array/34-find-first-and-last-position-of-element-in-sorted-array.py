class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        minIdx = float(inf)
        maxIdx = float(-inf)
        found = False
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                # find rightmost target
                found = True
                maxIdx = max(maxIdx, mid)
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                found = True
                # find leftmost target
                minIdx = min(minIdx, mid)
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        if found:
            return [minIdx, maxIdx]
        else:
            return [-1, -1]
