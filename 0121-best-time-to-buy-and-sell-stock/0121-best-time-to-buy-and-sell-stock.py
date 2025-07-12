class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        maxFromRight = [0] * n
        maxFromRight[n-1] = prices [n-1]

        for i in range(n -2, -1, -1):
            maxFromRight[i] = max(maxFromRight[i+1], prices[i])

        maxProfit = 0
        for i in range(n):
            maxProfit = max(maxProfit, maxFromRight[i] - prices[i])

        return maxProfit