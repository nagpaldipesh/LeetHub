class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num

        while low <= high:
            mid = low + (high - low) // 2

            square = mid * mid
            if  square == num:
                return True
            elif square > num:
                high = mid - 1
            else:
                low = mid + 1

        return False