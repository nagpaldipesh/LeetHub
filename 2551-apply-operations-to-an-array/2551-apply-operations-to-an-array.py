class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            if num == nums[i-1]:
                nums[i-1] , nums[i] = num * 2, 0

        zero_index = len(nums) -1
        result = [num for num in nums if num > 0]
        
        result.extend([0] * (len(nums) - len(result)))
        return result