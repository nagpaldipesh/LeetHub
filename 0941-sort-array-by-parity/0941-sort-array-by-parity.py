class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            if num % 2 == 0:
                result.append(num)
        
        for num in nums:
            if num % 2 == 1:
                result.append(num)
        
        return result
        # filtered = [num for num in nums if num % 2 == 0]
        # filtered.extend([num for num in nums if num not in filtered])

        # return filtered