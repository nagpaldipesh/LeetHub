class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter

        freq = Counter(arr)
        
        index = 0
        for key in freq:
            if freq[key] == 1:
                index += 1
            
            if index == k:
                return key 

        return ""