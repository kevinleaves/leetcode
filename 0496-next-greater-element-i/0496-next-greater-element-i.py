class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        '''
        i: 2 int[] nums where nums1 is a subset of nums2
        o: array with len(nums1), where res[i] is the next greater element found in nums2
        c: none
        e: 

        nums1 = [4,1,2]
        nums2 = [2,1,3,4]
        output = [-1, 3, 3]
        '''
        
        # create a mapping for nums1
        subset = {}
        for i, v in enumerate(nums1):
          subset[v] = i
        
        res = [0]*len(nums1)

        stack = []
        for i, v in enumerate(nums2):
          # if current v in nums1
            # if current v is > top of stack
            while stack and stack[-1] < v:
              indexInNums1 = subset[stack.pop()]
              res[indexInNums1] = v
            # add item to stack only if we need to
            if v in subset:
              stack.append(v)

        # empty the rest of the stack and fill it with -1s
        while stack:
          popped = stack.pop()
          res[subset[popped]] = -1

        return res