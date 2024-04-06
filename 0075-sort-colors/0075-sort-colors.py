class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # INSERTION SORT
        # TIME: O(N^2) Worst Case & Average Case. O(N) Best Case
        # SPACE: O(1) because in place.

        # start with the second index
        # compare current item with its preceding elements, stopping when it reaches an element it is smaller than
        # once we've found our insertion point, insert
        for i in range(1, len(nums)):
          tmp = nums[i]
          j = i - 1
          # break when nums[j] is smaller than tmp
          while j >= 0 and nums[j] > tmp:
            # shift elements to the right
            nums[j + 1] = nums[j]
            j -= 1
          # we have a hole to right of our current j. this is where tmp goes
          nums[j + 1] = tmp
        

            



        