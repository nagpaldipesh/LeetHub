class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)

        sorted_keys = sorted(freq, key= lambda x:(-freq[x]))
        return sorted_keys[:k]