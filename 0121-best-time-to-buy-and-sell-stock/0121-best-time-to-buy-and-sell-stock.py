class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       if (len(prices) == 0):
        return 0

       maxProfit = 0
       smallestPrice = prices[0]

       for price in prices:
        if price < smallestPrice:
            smallestPrice = price 
            continue

        maxProfit = max(maxProfit, price - smallestPrice)
       return maxProfit