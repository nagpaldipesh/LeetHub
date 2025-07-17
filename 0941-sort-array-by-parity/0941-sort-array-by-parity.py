class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_index = 0

        for i, num in enumerate(nums):
            if num % 2 == 0:
                nums[i], nums[even_index] = nums[even_index], nums[i]
                even_index += 1
            
        return nums

        # result = []

        # for num in nums:
        #     if num % 2 == 0:
        #         result.append(num)
        
        # for num in nums:
        #     if num % 2 == 1:
        #         result.append(num)
        
        # return result
        # filtered = [num for num in nums if num % 2 == 0]
        # filtered.extend([num for num in nums if num not in filtered])

        # return filtered