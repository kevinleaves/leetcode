class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #sort? in place?
        #create extra memory?
        #both are valid
        #make a counter, along with a hashmap
        mySet = set(range(1,len(nums)+1))
        
        for n in nums:
            if n in mySet:
                mySet.remove(n)
        
        return list(mySet)