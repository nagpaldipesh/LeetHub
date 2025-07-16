class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        words = s1.split() + s2.split()
        freq = Counter(words)

        return [k for (k, v) in freq.items() if v == 1]