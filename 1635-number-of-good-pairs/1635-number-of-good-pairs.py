class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map = {}

        count = 0 
        for num in nums:
            if num in map:
                count += map[num]
                map[num] += 1
            else:
                map[num] = 1

        return count