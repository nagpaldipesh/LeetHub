class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxNum = 0

        for i in reversed(range(0, len(prices))):

            profit = max(profit, maxNum - prices[i])

            #print(profit, maxNum, prices[i])
            if prices[i] > maxNum:
                maxNum = prices[i]
        
        return profit