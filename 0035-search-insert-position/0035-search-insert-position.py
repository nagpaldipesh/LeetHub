class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low  = 0
        high = len(nums) - 1

        result = high + 1
        while low <= high:
            mid = low + int((high - low) /2)

            num = nums[mid]
            if num == target:
                return mid
            elif num < target:
                low = mid + 1
            else:
                result = mid
                high = mid - 1
        
        return result