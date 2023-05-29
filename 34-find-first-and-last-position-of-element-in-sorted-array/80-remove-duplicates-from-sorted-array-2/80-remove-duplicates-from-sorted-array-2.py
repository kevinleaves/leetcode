class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i: int array nums sorted
        # o: length of the array with duplicates taken out
        # c: O(1) space. modify array in place
        # e:

        # r pointer scans input array. l pointer stays at the next possible slot in the resulting subarray
        count, l = 1, 1
        for r in range(1, len(nums)):
            # compare element at r pointer to r - 1, if they're the same, increment count otherwise we're at a unique value, reset the count
            if nums[r] == nums[r-1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[l] = nums[r]
                l += 1

        return l


