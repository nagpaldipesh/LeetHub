class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        maxSum = sumSoFar = nums[0]

        for i in range(1, n):
            if sumSoFar < 0:
                sumSoFar = 0
            
            sumSoFar += nums[i]

            if sumSoFar > maxSum:
                maxSum = sumSoFar
            
        return maxSum
        