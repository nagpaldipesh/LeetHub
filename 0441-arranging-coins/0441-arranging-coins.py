class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n
        result = 0

        while low <= high:
            mid = low + (high - low) // 2
            coins = mid * (mid + 1) // 2

            if n == coins:
                return mid
            elif n < coins:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result - 1 # last row is incomplete
