class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        filtered = [num for num in nums if num % 2 == 0]
        filtered.extend([num for num in nums if num not in filtered])

        return filtered