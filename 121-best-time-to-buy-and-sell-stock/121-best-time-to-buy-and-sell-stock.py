class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #returning the max difference between an index and a > index
        #3 variables
        #start day, end day, difference = price[end]-price[start]
        res = 0
        start, diff = 0, 0
        for end in range(0,len(prices)):
            diff = prices[end]-prices[start]
            if prices[start] > prices[end]:
                start = end
            if diff > res:
                res = diff
        return res