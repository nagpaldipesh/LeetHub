class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)

        for (k,v) in freq.items():
            if v == 1:
                return s.index(k)

        return -1