class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1

                if count > 1:
                    return False
        
        return True
        # is_rotated = False

        # for i in range(1, len(nums)):
        #     if(is_rotated):
        #         if nums[i] < nums[i-1] or nums[i] > nums[0]:
        #             return False
        #     else:
        #         if nums[i] < nums[i-1]:
        #             if nums[i] > nums[0]:
        #                 return False
        #             is_rotated = True
            

        # return True