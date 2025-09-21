class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = sumSoFar = nums[0]

        for i in range(1, len(nums)):
            
            sumSoFar = max(nums[i], sumSoFar + nums[i])
            
            if sumSoFar > maxSum:
                maxSum = sumSoFar

        return maxSum