class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        for index in range(0, n):
            total += nums[index]
        
        left_sum = 0
        for i in range(0, n):
            right_sum = total - left_sum - nums[i]
            
            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
