class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        #sorted_freq = sorted(freq.items(), key=lambda x: -x[1])
        mostcommon = freq.most_common()

        result = []
        for (k,v) in mostcommon:
            result.extend(k*v)

        return ''.join(result)