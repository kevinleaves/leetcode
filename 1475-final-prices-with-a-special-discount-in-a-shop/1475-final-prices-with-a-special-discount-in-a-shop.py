class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
      '''
      i: prices[] of i items
      o: int[] of final prices for the items in prices[] after possible discounts
      c: none
      e: there are no discounts

      USE A STACK
      O(N) time
      O(N) space
      '''

      stack = []

      for i, v in enumerate(prices):
        while stack and prices[stack[-1]] >= v:
          poppedIndex = stack.pop()
          prices[poppedIndex] -= v
        # add indices to the stack
        stack.append(i)

      return prices
