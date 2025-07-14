class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        min_freq = [float('inf')] * 26
        base = ord('a')
        
        for word in words:
            freq = Counter(word)
            for i in range(26):
                char = chr(i + base)
                min_freq[i] = min(min_freq[i], freq[char])
        
        result = []
        for i in range(26):
            if min_freq[i] > 0:
                result.extend([chr(i + base)] * min_freq[i])
        
        return result
