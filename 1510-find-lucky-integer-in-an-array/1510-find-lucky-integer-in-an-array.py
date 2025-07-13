class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter

        freq = Counter(arr)
        lucky = -1
        for key in freq:
            if key == freq[key] and key > lucky:
                lucky = key
        
        return lucky
        