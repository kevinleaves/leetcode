class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        i: array of prices of given stock on the ith day
        o: int max profit we can achieve in 1 transaction, return 0 if no profit can be gained
        c: none
        e: can't return profit -> return 0. if array length is 1, return 0 because we can't buy and sell on
        the same day
        '''

        maxProfit = 0

        # 2 pointers
        # keep a pointer at the minimum price we see
        # if current pointer - min > maxProfit, update max profit

        l, r = 0, 0
        minPrice = prices[l]
        # while indices are in bounds
        while l < len(prices) and r < len(prices):
          # update minimum price
          if prices[r] < minPrice:
            minPrice = prices[r]
            l = r

          currProfit = prices[r] - prices[l]
          maxProfit = max(maxProfit, currProfit)
          r += 1

        return maxProfit