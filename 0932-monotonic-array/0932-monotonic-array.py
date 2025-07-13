class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n =  len(nums)

        #increasing_count = decreasing_count = 0
        increasing = decreasing = False
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                increasing = True
            elif nums[i] < nums[i-1]:
                decreasing = True
        
        return not increasing or not decreasing
