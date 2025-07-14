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

        for i, freq in enumerate(min_freq):
            #print(freq)
            if freq > 0:
                c = chr(i+sub)
                for j in range(freq):
                    result.append(c)

        # return list(c if freq > 0 for i, freq in enumerate(min_freq))

        return result
