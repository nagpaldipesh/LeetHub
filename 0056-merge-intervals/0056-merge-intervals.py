class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for start, end in intervals:
            lastStart, lastEnd = result[-1]

            if (start > lastEnd):
                result.append([start, end])
            else:
                result[-1][1] = max(lastEnd, end)
        
        return result