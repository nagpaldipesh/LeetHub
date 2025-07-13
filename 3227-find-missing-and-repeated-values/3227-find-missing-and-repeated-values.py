class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) * len(grid) + 1

        is_present = [False] * n
        result = []

        for row in grid:
            for num in row:
                if is_present[num]:
                    result.append(num)
                
                is_present[num] = True

        for i in range(1, n):
            if not is_present[i]:
                result.append(i)
                break

        return result