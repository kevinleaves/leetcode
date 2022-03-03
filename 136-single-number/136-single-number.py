class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #length of the array MUST be odd
        dictionary = {}
        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        
        for i in dictionary:
            if dictionary[i] == 1:
                return i
        
                