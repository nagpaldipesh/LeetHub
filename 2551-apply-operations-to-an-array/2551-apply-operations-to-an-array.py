class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] , nums[i] = nums[i-1] * 2, 0

        result = [num for num in nums if num != 0]
        
        result.extend([0] * (len(nums) - len(result)))
        return result