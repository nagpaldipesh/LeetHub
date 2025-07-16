class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nonZeroIndex = 0
        start = 0
        end = len(nums) - 1

        while start <= end:
            if nums[start] != 0:
                nums[start], nums[nonZeroIndex] = nums[nonZeroIndex], nums[start]
                nonZeroIndex += 1
            start += 1
            