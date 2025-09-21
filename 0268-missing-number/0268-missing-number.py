class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = len(nums)
        sum = 0 

        for index, num in enumerate(nums):
            expectedSum += index
            sum += num
        
        return expectedSum - sum