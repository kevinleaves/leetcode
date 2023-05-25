class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            # we found our target, return index
            if nums[mid] == target:
                return mid

            # left sorted portion
            if nums[mid] >= nums[l]:
                # search for target within this portion of the array
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # right sorted portion
            else:
                # search for target within the right portion of the array
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
