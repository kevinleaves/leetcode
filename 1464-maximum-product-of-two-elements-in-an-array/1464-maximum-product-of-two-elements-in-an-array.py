class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        brute force check pairs and store a max product
        O(N^2) TIME
        O(1) SPACE

        sort array in non-decreasing order, use the last two elements to compute result
        O(nlogn) TIME
        O(1) SPACE
        '''
        nums.sort()
        return (nums[-1]-1) * (nums[-2]-1)