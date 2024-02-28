class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        template:
        init res
        expand window
        contract window when x condition
          find out where left goes

        update max/maintain answer/diff btwn right and left
        return res
        '''

        left = 0
        maxProfit = 0
        for i, price in enumerate(prices):
          currProfit = prices[i] - prices[left]
          if currProfit < 0:
            # contract window, move left pointer. where? +1? 
            # no, shift it all the way over to i, because we want left to be pointing to the lowest possible number
            left = i

          maxProfit = max(maxProfit, currProfit)

        return maxProfit
