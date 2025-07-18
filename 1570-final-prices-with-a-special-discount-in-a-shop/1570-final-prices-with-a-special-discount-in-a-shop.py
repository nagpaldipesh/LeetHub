class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = [0] * n       
        stack = []

        for num in reversed(prices):
            
            while len(stack) > 0 and stack[-1] > num:
                stack.pop()
            
            result[n-1] = num - stack[-1] if len(stack) > 0 else num
            
            stack.append(num)
            n -= 1

        return result
