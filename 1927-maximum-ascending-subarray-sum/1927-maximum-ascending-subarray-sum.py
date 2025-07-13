class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        maxSum = sumSoFar = nums[0]

        for i in range(1, n):
            num = nums[i]

            if num > nums[i-1]:
                sumSoFar += num
            else:
                sumSoFar = num
            
            maxSum = max(maxSum, sumSoFar)

        return maxSum