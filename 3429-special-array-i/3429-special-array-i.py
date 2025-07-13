class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if(len(nums) == 0):
            return False

        isEven = not nums[0] % 2 == 0

        for i in range( 1, len(nums)):
            num = nums[i]
            if isEven:
                if num % 2 == 1:
                    return False
            else:
                if num % 2 == 0:
                    return False
            
            isEven = not isEven
        
        return True
        