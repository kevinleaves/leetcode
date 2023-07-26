class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

        i: 2 nums arrays, m, n representing # elements in the arrays
        o: nums1 filled with items from nums2. sorted
        c: O(m + n) time
        e: 
        """

        '''
        l                   
        1 2 3 0 0 0         2 5 6
        '''
        
        # set pointers
        fill = m + n - 1
        left = m - 1
        right = n - 1

        # while loops to merge 
        # all elements are exhausted
        while fill >= 0 and right >= 0 and left >= 0:
            if nums1[left] > nums2[right]:
                nums1[fill] = nums1[left]
                left -= 1
                fill -= 1
            else:
                # exhaust right faster because we exhaust right when it's larger AND when both elements are equal
                nums1[fill] = nums2[right]
                right -= 1
                fill -= 1
        
        # haven't exhausted left yet, handle that
        while left >= 0:
            nums1[fill] = nums1[left]
            left -= 1
            fill -= 1

        while right >= 0:
            nums1[fill] = nums2[right]
            right -= 1
            fill -= 1
            
        return nums1

