class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter

        freq = Counter(arr)
        lucky = -1
        for key, count in freq.items():
            if key == count and key > lucky:
                lucky = key
        
        return lucky
        