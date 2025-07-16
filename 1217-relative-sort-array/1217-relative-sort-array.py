class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(arr1)

        result = []

        for num in arr2:
            result.extend([num] * freq[num])
            
        remaining = []
        for (k, v) in freq.items():
            if k not in arr2:
                remaining.extend([k] * v)

        result.extend(sorted(remaining))
        return result