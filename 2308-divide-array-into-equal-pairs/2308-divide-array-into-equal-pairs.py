class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter

        freq = Counter(nums)

        for value in freq.values():
            if value % 2 == 1:
                return False
        
        return True