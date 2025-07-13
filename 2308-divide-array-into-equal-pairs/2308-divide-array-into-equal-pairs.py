class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter

        # freq = Counter(nums)

        # for value in freq.values():
        #     if value % 2 == 1:
        #         return False
        
        # return True

        return all(count % 2 == 0 for count in Counter(nums).values())