class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}

        for i, num in enumerate(nums):
            if num in map:
                if abs(i - map[num]) <= k:
                    return True
            
            map[num] = i
        return False