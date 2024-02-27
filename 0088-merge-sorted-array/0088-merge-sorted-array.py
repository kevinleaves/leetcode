class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        i: 2 nums arrays
        o: 
        c:
        e:

        read elements from right to left from both sides of the array

        write pointer starts at the end of the array
        when we successfully write using an element from either array,
        we decrement that pointer
        need conditions to ensure that every original number in both arrays is written once
        write until write pointer is < 0

        """

        r1 = m - 1 # 2
        r2 = n - 1 # 2
        w1 = len(nums1) - 1 # 5

        while w1 >= 0 and r1 >= 0 and r2 >= 0:
          # fill in spots at w1 with elements from n1 or n2 depending on which is larger
          # compare elements at r1 and r2
          if nums2[r2] >= nums1[r1]:
            nums1[w1] = nums2[r2]
            r2 -= 1
          else:
          # if first number is larger
            nums1[w1] = nums1[r1]
            r1 -= 1

          w1 -= 1
          # conditions to exhaust either array if they have leftover elements
          # we've exhausted r2, fill in the rest of the elements from n1

        while r2 >= 0:
          nums1[w1] = nums2[r2]
          r2 -= 1
          w1 -= 1

                  
                  
          



        
