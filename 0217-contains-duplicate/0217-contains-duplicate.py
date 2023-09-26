class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        i: int[]
        o: boolean
        c: o(n) space o(n) time
        e: negative integers. nums array is empty

        instantiate empty set
        iterate through nums
            if current element is in set
                return true
            else
                add element to set

        return false
        '''
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
