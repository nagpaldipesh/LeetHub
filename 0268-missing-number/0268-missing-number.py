class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        totalSum = 0
        expectedSum = 0

        for index, num in enumerate(nums):
            totalSum += num
            expectedSum += index+1
        

        return expectedSum - totalSum