class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        right_sum = 0

        for index in range(0, n):
            right_sum += nums[index]
        
        left_sum = 0

        for i in range(0, n):
            right_sum -= nums[i]
            
            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
