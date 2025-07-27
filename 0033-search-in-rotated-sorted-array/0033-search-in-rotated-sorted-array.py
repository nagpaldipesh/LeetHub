class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivotIndex(arr: List[int]) -> int:
            low, high = 0, len(arr) - 1
            result = 0

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] >= nums[0]:
                    low = mid + 1
                else:
                    result = mid
                    high = mid - 1
            
            return result

        def binarySearch(arr: List[int], tar: int, low: int, high: int) -> int:

            while low <= high:
                mid = low + (high - low) //2
                num = nums[mid]

                if num == tar:
                    return mid
                elif num > tar:
                    high = mid - 1
                else:
                    low = mid + 1
                
            return -1

        pivot = findPivotIndex(nums)

        if nums[pivot] <= target <= nums[-1]:
            return binarySearch(nums, target, pivot, len(nums) - 1)
        else:
            return binarySearch(nums, target, 0, pivot - 1)