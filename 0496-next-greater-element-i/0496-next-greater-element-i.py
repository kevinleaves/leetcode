class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        return an array of length == nums1
        n representing len(nums1)
        perform n number of queries on nums2 array
        for each item in nums1,
          search for item in nums2 and find the next greater element to the right of it.
          if we don't find one, query returns -1
        '''
        # time: O(n x k) where n is the length of n1 and k is the length of n2
        # space: O(1)
        res = [0]*len(nums1)
        
        for i, v1 in enumerate(nums1):
          for j, v2 in enumerate(nums2):
            if v2 == v1:
              found = False
              for k in range(j, len(nums2)):
                if nums2[k] > v1:
                  res[i] = nums2[k]
                  found = True
                  break
              if not found:
                res[i] = -1

        return res
