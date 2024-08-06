class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
      '''
      i: prices[] of i items
      o: int[] of final prices for the items in prices[] after possible discounts
      c: none
      e: there are no discounts
      '''

      res = [0]*len(prices)
      for l in range(len(prices)):
        discount = 0
        for r in range(l+1, len(prices)):
          if prices[r] <= prices[l]:
            discount = prices[r]
            break
        res[l] = prices[l] - discount
        
      return res