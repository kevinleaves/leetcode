from functools import reduce

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        '''
        product => product of all values in nums array
        return signFunc(product)
        signFunc(x: int) -> int

        i: nums array (+ & - int)
        o: 1, 0, -1
        c: none
        e: 

        if the product is positive, return 1, 
        if the product is negative, return -1
        if the product is 0, return 0

        find product
        return int


        '''
        
        product = reduce((lambda x, y: x * y), nums)
        # product2 = 1
        # for num in nums:
        #     product2 *= num
        # print(product, product2)
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0