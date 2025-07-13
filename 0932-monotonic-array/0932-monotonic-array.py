class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n =  len(nums)

        increasing_count = decreasing_count = 0

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                increasing_count += 1
            elif nums[i] < nums[i-1]:
                decreasing_count += 1
        
        return increasing_count == 0 or decreasing_count == 0
