class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        uniqueIndex = 0

        for index in range(1, len(nums)):

            if(nums[index] != nums[index - 1]):
                uniqueIndex += 1
                nums[uniqueIndex] = nums[index]

        
        return uniqueIndex + 1