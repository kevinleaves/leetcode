class Solution: # 87.32%, 89.5%
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # leftProduct as 1
        # rightProduct as 1
        # res array

        leftProd = 1
        rightProd = 1
        res = len(nums)*[0]

        # 1st loop: populate res with left products. populate res first then update leftProd
        for i, num in enumerate(nums):
            res[i] = leftProd
            leftProd *= num

        # 2nd loop: iterate backwards. multiply left prods with right prods. set then update rightProd
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= rightProd
            rightProd *= nums[i]

        return res
