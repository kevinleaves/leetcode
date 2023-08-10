class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        o: ans array len 2n, populated with 

        nums [1,2,1]
        ans  [1,2,1,]
        012
        n = 3
        ans[3] => nums[0]
        ans[1+3] => nums[1]
        ans[2+3] => nums[2]

        '''
        res = len(nums)*2*[0]

        for i in range(len(nums)*2):
            if i < len(nums):
                res[i] = nums[i]
            else:
                res[i] = nums[i - len(nums)]
                
        return res

        