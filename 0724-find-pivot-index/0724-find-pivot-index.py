class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pefixSum = [0] * n
        pefixSum[0] = nums[0]

        for index in range(0, n):
            pefixSum[index] = nums[index] + pefixSum[index -1]

        total = pefixSum[n-1]
        for i in range(0, n):
            left_sum = 0 if i == 0 else pefixSum[i-1]
            right_sum = 0 if i == n-1 else total - pefixSum[i]
            
            if left_sum == right_sum:
                return i

        return -1
