class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        nums = set()
        result = []

        for row in grid:
            for num in row:
                if num in nums:
                    result.append(num)
                
                nums.add(num)

        for i in range(1, len(grid) * len(grid) + 1):
            if i not in nums:
                result.append(i)

        return result