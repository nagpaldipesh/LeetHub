class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        ransomNote_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)

        return all( k in magazine_freq and magazine_freq[k] >= v for (k,v) in ransomNote_freq.items())