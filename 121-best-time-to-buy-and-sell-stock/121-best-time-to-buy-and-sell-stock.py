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
            
        
        