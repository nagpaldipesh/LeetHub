class Solution:
    def check(self, nums: List[int]) -> bool:
        
        is_rotated = False

        for i in range(1, len(nums)):
            if(is_rotated):
                if nums[i] < nums[i-1] or nums[i] > nums[0]:
                    return False
            else:
                if nums[i] < nums[i-1]:
                    if nums[i] > nums[0]:
                        return False
                    is_rotated = True
            

        return True