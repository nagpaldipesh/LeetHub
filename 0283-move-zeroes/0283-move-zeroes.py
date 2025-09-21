class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        indexToSwap = 0

        for index, num in enumerate(nums):
            if num != 0:
                nums[index], nums[indexToSwap] = nums[indexToSwap], nums[index]
                indexToSwap += 1
        
