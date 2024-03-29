class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # pointer
        # container to hold current value?
        # create another array to store seen?
        # create a dictionary to store seen?
        myDict = {}
        for idx, value in enumerate(nums):
            if value not in myDict:
                myDict[value] = idx
            else:
                return True
        return False


# n log n solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


# brute force n^2 (TLE)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
