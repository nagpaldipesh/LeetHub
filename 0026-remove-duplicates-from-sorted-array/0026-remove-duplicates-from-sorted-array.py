class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        uniqueIndex = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[uniqueIndex]:
                uniqueIndex += 1
                nums[uniqueIndex] = nums[i]
        
        return uniqueIndex + 1