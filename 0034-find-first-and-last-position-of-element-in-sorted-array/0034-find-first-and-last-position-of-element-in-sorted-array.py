class Solution:
    def searchRange(self, nums1: List[int], target: int) -> List[int]:
        
        def findFirstOccurence(nums: List[int]) -> int:
            low, high = 0, len(nums) - 1
            result = -1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    result = mid
                    high = mid - 1 
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return result
        

        def findLastOccurence(nums: List[int]) -> int:
            low, high = 0, len(nums) - 1
            result = -1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    result = mid
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return result
        

        return [findFirstOccurence(nums1), findLastOccurence(nums1)]
        
