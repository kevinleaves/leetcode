class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointers
        #start, end
        #end iterates through prices
        #move start pointer when we find the new lowest price
        res, start, diff = 0, 0, 0
        for end in range(len(prices)):
            diff = prices[end] - prices[start]
            if diff < 0:
                start = end
            res = max(res, diff)
        return res

class Solution: # 71.82% 80.39%
    def maxProfit(self, prices: List[int]) -> int:
        # min is usually initialized as the first value of an iterable
        minPrice = prices[0]
        # this is our result
        maxPrice = 0

        for i in range(len(prices)):
            currPrice = prices[i]
            # compare current price to the current minimum. we want to find the largest range so we track min
            if currPrice < minPrice:
                minPrice = currPrice
            # calculate max possible price
            maxPrice = max(maxPrice, currPrice - minPrice)
        return maxPrice


