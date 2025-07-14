class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        min_freq = [1000] * 26
        sub = ord('a')
        
        from collections import Counter

        for word in words:
            freq = Counter(word)

            for i in range(26):
                c = chr(i+sub)
                min_freq[i] = min(min_freq[i], freq[c])

        result = []

        for i in range(26):
            #print(freq)
            freq = min_freq[i]
            if freq > 0:
                c = chr(i+sub)
                result.extend(c * freq)

        # return list(c if freq > 0 for i, freq in enumerate(min_freq))

        return result
